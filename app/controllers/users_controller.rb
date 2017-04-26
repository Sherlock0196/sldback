class UsersController < ApplicationController

  require 'rubypython'
  require 'csv'

  def index
    @users = User.all
  end

  def bar
    data = Lawder::LoadData::Data
    arg = [[1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],[1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,0],
          [1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0], [1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0],
           [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]
    output = `python #{Rails.root}/lib/assets/smach.py '#{data}' '#{arg}'`
    logger.debug output
    puts "wow"

  end
end
