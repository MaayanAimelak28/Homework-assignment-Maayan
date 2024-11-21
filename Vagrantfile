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
      # Install Apache web server, configure the web page and start the service
      srv.vm.provision "shell", inline: <<-SHELL
        sudo yum install httpd wget vim unzip zip -y
        sudo systemctl start httpd
        sudo systemctl enable httpd
        cd /var/www/html/
        sudo touch index.html
        sudo echo '<h1>#{server[:message]}</h1>' > index.html
        sudo systemctl restart httpd
      SHELL
    end
  end

  # Nginx server
  config.vm.define "nginx" do |srv|
    srv.vm.box = "eurolinux-vagrant/centos-stream-9"
    srv.vm.network "private_network", ip: "192.168.56.24"
    srv.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
    srv.vm.provision "shell", inline: <<-SHELL
      # Install Docker
      sudo yum install -y yum-utils
      sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
      sudo yum install -y docker-ce docker-ce-cli containerd.io
      sudo systemctl start docker
      sudo systemctl enable docker
      # Create the nginx configuration
      cat <<EOL > /tmp/nginx.conf
      events {}
      http {
        upstream backend {
          server 192.168.56.19:80;
          server 192.168.56.20:80;
        }
        server {
          listen 80;
          location / {
            proxy_pass http://backend;
          }
        }
      }
EOL
      # Run the nginx container with the configuration file
      sudo docker run -d --name nginx -p 80:80 -v /tmp/nginx.conf:/etc/nginx/nginx.conf:ro nginx
    SHELL
    end
end