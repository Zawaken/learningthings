#!/bin/perl
$c=0;
while(++$c<100)
{
	if($c % 3 != 0 and $c % 5 != 0) {print "$c";}
	if($c % 3 == 0) { print "fizz";}
	if($c % 5 == 0) { print "buzz";}
	print "\n";
}
