#!/usr/bin/env ruby
MatchValue = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
puts ARGV[0].scan(MatchValue).join(",")
