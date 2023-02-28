Vagrant.configure("2") do |config|

  nodes = [
    { name: "master", ip: "192.168.56.10" },
    { name: "worker", ip: "192.168.56.11" }
  ]

  nodes.each do |node|
    config.vm.define node[:name] do |n|
      n.vm.box = "ubuntu/focal64"

      n.vm.provision :docker
      n.vm.provision "shell", inline: <<-SHELL
        sudo sed -i 's/^\\s*PasswordAuthentication\\s\\+no/PasswordAuthentication yes/' /etc/ssh/sshd_config
        sudo systemctl restart sshd.service
      SHELL

      n.vm.network "private_network", ip: node[:ip]
      n.vm.hostname = node[:name]
    end
  end
end