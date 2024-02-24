# kill_process.pp
# script to execute a command using puppet
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin/'
}
