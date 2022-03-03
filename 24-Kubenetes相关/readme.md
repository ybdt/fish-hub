# 获取当前集群下全部node
.\kubectl -s 172.31.32.36:8089 get nodes
# 获取node详细信息
.\kubectl -s 172.31.32.36:8089 describe node 10-8-0-135
# 获取当前节点下全部pod
.\kubectl -s 172.31.32.36:8089 get pods
# 获取直接pod详细信息
.\kubectl -s 172.31.32.36:8089 describe pod wpsai-apollo-adminservice-744b6bddcd-hdngw

# 获取cluster ip
.\kubectl.exe -s 172.31.32.36:8089 -n default get service  
.\kubectl.exe -s 172.31.32.36:8089 get pods -o wide  
--kubelet-client-certificate=ca.crt --kubelet-client-key=token.txt  
.\kubectl.exe -s 172.31.32.36:8089 --namespace=default exec -it wpsai-apollo-adminservice-744b6bddcd-hdngw bash  
.\kubectl.exe -s 172.31.32.36:8089 create clusterrolebinding kube-apiserver:kubelet-apis --clusterrole=system:kubelet-api-admin --user=system:anonymous  
.\kubectl -s 172.31.32.36:8089 create clusterrolebinding kube-apiserver:kubelet-apis --clusterrole=system:kubelet-api-admin --user kubernetes-master  
.\kubectl -s 172.31.32.36:8089 describe pod/wpsai-apollo-adminservice-744b6bddcd-hdngw -n default  