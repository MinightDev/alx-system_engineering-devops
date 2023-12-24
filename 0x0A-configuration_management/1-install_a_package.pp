# 1-install_a_package.pp

# Puppet manifest to install Flask package (version 2.1.0) using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
