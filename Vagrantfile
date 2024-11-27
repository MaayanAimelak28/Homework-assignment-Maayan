Vagrant.configure("2") do |config|
  # The web servers
  servers = [
    { name: "web1", ip: "192.168.56.19", message: "Hello from server 1" },
    { name: "web2", ip: "192.168.56.20", message: "Hello from server 2" }
  ]
  # Loop over each server to define and configure the settings
  servers.each do |server|
    config.vm.define server[:name] do |srv|
      srv.vm.box = "eurolinux-vagrant/centos-stream-9"
      srv.vm.network "private_network", ip: server[:ip]
      srv.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
      end
      srv.vm.provision "ansible" do |ansible|
        ansible.playbook = web_playbook.yaml
        ansible.limit = server[:name]
        ansible.extra_vars = {
          server_message: server[:message]
        }
      end
    end
  end

  # Nginx server
  config.vm.define "nginx" do |srv|
    srv.vm.box = "eurolinux-vagrant/centos-stream-9"
    srv.vm.network "private_network", ip: "192.168.56.24"
    srv.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
    srv.vm.provision "ansible" do |ansible|
      ansible.playbook = nginx_playbook.yaml
      ansible.limit = "nginx"
    end
end