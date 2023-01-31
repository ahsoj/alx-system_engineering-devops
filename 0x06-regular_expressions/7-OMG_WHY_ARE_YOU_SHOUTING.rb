#!/usr/bin/env ruby
MatchValue = /[A-Z]*/
puts ARGV[0].scan(MatchValue).join
