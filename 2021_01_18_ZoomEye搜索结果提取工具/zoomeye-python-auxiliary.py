def main():
    with open("网康下一代防火墙_20_1618384827.json", "r") as f_r:
        with open("ip.txt", "w") as f_w:
            lines = f_r.readlines();
            for line in lines:
                protocol = line.split()[5].strip("}").strip("'");
                ip = line.split()[1].strip(",").strip("'");
                port = line.split()[3].strip(",");
                f_w.write(protocol + "://" + ip + ":" + port + "\n");

main();
