module Lawder
  require 'csv'
  class LoadData
      file = File.read("#{Rails.root}/lib/assets/data.csv")
      @dataset = CSV.parse(file)
      Data = @dataset.map!{|i| i.map! {|x| x.to_i} }
  end
end

Lawder::LoadData::Data
