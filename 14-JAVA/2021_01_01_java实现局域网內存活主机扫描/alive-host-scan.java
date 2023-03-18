package package0;

import java.net.InetAddress;

public class AliveHostScan {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		String start_ip = "10.133.80.";
		String ip = null;
		int sum = 0;
		for (int i = 0; i <= 256; i++) {
			ip = start_ip + i;
			InetAddress address = InetAddress.getByName(ip);
			if (address.isReachable(5000)) {
				System.out.println("                    host " + ip + " is reachable");
				sum += 1;
			}
			else {
				System.out.println("host " + ip + " is unreachable");
			}
		}
		System.out.println("ALL the hosts are: " + sum);
	}

}
