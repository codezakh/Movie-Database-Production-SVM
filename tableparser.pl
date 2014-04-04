
#the following piece of code reads the whole file into a string

local $/;
open(FILE, 'main.html.1') or die "Can't read file 'filename' [$!]\n";  
$html_string = <FILE>; 
close (FILE);  
#print $document;


# Matched tables are returned as table objects; tables can be matched
 # using column headers, depth, count within a depth, table tag
 # attributes, or some combination of the four.

 # Example: Using column header information.
 # Assume an HTML document with tables that have "Date", "Price", and
 # "Cost" somewhere in a row. The columns beneath those headings are
 # what you want to extract. They will be returned in the same order as
 # you specified the headers since 'automap' is enabled by default.

 use HTML::TableExtract;
 $te = HTML::TableExtract->new( headers => [qw(@)] );
 $te->parse($html_string);

 # Examine all matching tables
 foreach $ts ($te->tables) {
   print "Table (", join(',', $ts->coords), "):\n";
   foreach $row ($ts->rows) {
      print join(',', @$row), "\n";
   }
 }

 # Shorthand...top level rows() method assumes the first table found in
 # the document if no arguments are supplied.
 foreach $row ($te->rows) {
    print join(',', @$row), "\n";
 }

 # Example: Using depth and count information.
 # Every table in the document has a unique depth and count tuple, so
 # when both are specified it is a unique table. Depth and count both
 # begin with 0, so in this case we are looking for a table (depth 2)
 # within a table (depth 1) within a table (depth 0, which is the top
 # level HTML document). In addition, it must be the third (count 2)
 # such instance of a table at that depth.

 # $te = HTML::TableExtract->new( depth => 2, count => 2 );
 # $te->parse_file($html_file);
 # foreach $ts ($te->tables) {
 #    print "Table found at ", join(',', $ts->coords), ":\n";
 #    foreach $row ($ts->rows) {
 #       print "   ", join(',', @$row), "\n";
 #    }
 # }