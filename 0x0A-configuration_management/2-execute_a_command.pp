# kill_process.pp

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}
