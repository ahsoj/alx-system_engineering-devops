#!/usr/bin/env ruby
MatchValue = /h[\w]n/
puts ARGV[0].scan(MatchValue).join