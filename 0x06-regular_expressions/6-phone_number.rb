#!/usr/bin/env ruby
MatchValue = /^\d{10,10}$/
puts ARGV[0].scan(MatchValue).join
