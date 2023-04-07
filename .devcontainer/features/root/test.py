def test_awscli_is_installed(host):
  cmd = host.run("aws --version")
  assert cmd.stdout.startswith("aws-cli")
