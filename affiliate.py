#!/usr/bin/env python3
"""Number affiliations for each author, given an author list with affiliations
for each author."""

import argparse
from collections import OrderedDict

__author__ = 'Hayden Metsky <hayden@mit.edu>'


def read_authors(fn):
    """Read list of authors and shortcuts of their affiliations.

    Args:
        fn: path to file with two columns in which each line corresponds
            to an author; column 1 gives the author's name and column
            2 gives a comma-separated list of shorthand names of their
            affiliations

    Returns:
        ordered dict {author name: list of shorthands for affiliations},
        where the order of authors is the same as in the given file
    """
    authors = OrderedDict()
    with open(fn) as f:
        for line in f:
            author, affiliations = line.strip().split('\t')
            affiliations = affiliations.split(',')
            authors[author] = affiliations
    return authors


def read_affiliations(fn):
    """Read list of full names of affiliations.

    Args:
        fn: path to file with two columns in which each line corresponds
            to an affiliation; column 1 gives a shorthand name for the
            affiliation (assigned to authors) and column 2 gives the
            full name of the affiliation

    Returns:
        dict {shorthand for affiliation: full name of affiliation}
    """
    affiliations = {}
    with open(fn) as f:
        for line in f:
            shorthand, fullname = line.rstrip().split('\t')
            affiliations[shorthand] = fullname
    return affiliations


def main(args):
    # Read input
    authors = read_authors(args.authors)
    affiliations = read_affiliations(args.affiliations)

    # Verify that each author's affiliation has a name
    for author in authors:
        for affiliation in authors[author]:
            if affiliation not in affiliations:
                raise Exception(("Author %s has affiliation %s but the "
                    "name of that affiliation was not given") % (author,
                    affiliation))

    # Order affiliations according to the author order
    affiliations_number = {}
    curr_num = 1
    for author in authors:
        for affiliation in authors[author]:
            if affiliation not in affiliations_number:
                affiliations_number[affiliation] = curr_num
                curr_num += 1
    affiliations_ordered = sorted(list(affiliations.keys()),
        key=lambda x: affiliations_number[x])

    # Generate HTML of authors with their affiliations numbered
    author_html = ''
    for i, author in enumerate(authors):
        numbers = [affiliations_number[x] for x in authors[author]]
        numbers_str = ','.join([str(x) for x in sorted(numbers)])
        if i > 0:
            author_html += ', '
        author_html += author + '<sup>' + numbers_str + '</sup>'

    # Generate HTML of affiliations with their full names
    affiliations_html = ''
    for i, affiliation in enumerate(affiliations_ordered):
        number = str(affiliations_number[affiliation])
        fullname = affiliations[affiliation]
        if i > 0:
            affiliations_html += ' '
        affiliations_html += '<sup>' + number + '</sup>' + fullname + '.'

    # Write HTML
    with open(args.out, 'w') as f:
        f.write(author_html)
        f.write('<br><br>')
        f.write(affiliations_html)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('authors',
        help=("Path to file in which each line corresponds to an author "
              "(ordered as desired) and there are 2 columns: column 1 "
              "gives the full name of the author and column 2 gives a "
              "shorthand for the author's affiliation"))
    parser.add_argument('affiliations',
        help=("Path to file in which each line corresponds to an affiliation "
              "and there are 2 columns: column 1 gives a shorthand for an "
              "affiliation and column 2 gives the full name of the "
              "affiliation"))
    parser.add_argument('out',
        help=("Path to output HTML file that gives an author list with "
              "numbered affiliations"))

    args = parser.parse_args()
    main(args)
