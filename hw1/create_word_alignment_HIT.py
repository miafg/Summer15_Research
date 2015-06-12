#!/usr/bin/python
import os
import sys
import csv
import codecs

def main():
    """    
    Creates a CSV file as input to the word-alignment HIT.
    """
    annotated_test_set_file = open(sys.argv[1], "r").readlines()
    csv_output_file = open(sys.argv[2], "w")
    csv_writer = csv.writer(csv_output_file)
    headers = ["source", "target", "sureAlignments", "possAlignments", "sourceHighlights", "targetHighlights", "docID", "sentID", "wordCompressionRatio", "charCompressionRatio"]
    csv_writer.writerow(headers)

    possAlignments = ""
    sourceHighlights = ""
    targetHighlights = ""
    for line in annotated_test_set_file:
        line = line.strip()
        (source, target, sureAlignments, docID, sentID, wordCR, charCR) =  line.split(" ||| ")
        source = source.replace('"', '&quot;')
        target = target.replace('"', '&quot;')
        source = source.replace("'", '&apos;')
        target = target.replace("'", '&apos;')
        csv_writer.writerow([source, target, sureAlignments, possAlignments, sourceHighlights, targetHighlights, docID, sentID, wordCR, charCR])


if __name__ == "__main__":
    main()



