#!/usr/bin/env ruby
MatchValue = /hbt{2,5}n/
puts ARGV[0].scan(MatchValue).join