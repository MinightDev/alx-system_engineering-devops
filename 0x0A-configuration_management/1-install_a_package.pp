# 1-install_a_package.pp

class { 'python':
  version => 'system',
}

class { 'python::pip':
  ensure => 'latest',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Class['python::pip'],
}

