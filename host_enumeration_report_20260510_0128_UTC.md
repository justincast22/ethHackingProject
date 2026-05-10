# Host Enumeration Report

Generated: 2026-05-10 01:32 UTC

---

## Host: 127.0.0.1

### Verified Information

| Field | Value |
|---|---|
| IP Address | 127.0.0.1 |
| Hostname | localhost |
| Domain | Unknown |
| Operating System | Unknown |
| Active Services | mysql (3306/tcp) - 5000/tcp  open  upnp<br>afs3-fileserver (7000/tcp) - 28201/tcp open  unknown<br>rtsp (5000/tcp) - |_rtsp-methods: ERROR: Script execution failed (use -d to debug)<br>pharos (28201/tcp) - Pharos Notify (printing client)<br>mysqlx (33060/tcp) - MySQL X protocol listener<br>unknown (49344/tcp) - 50327/tcp open     unknown<br>bandwidth-test (56761/tcp) - MikroTik bandwidth-test server |
| Windows-Specific Information | None detected |

### Unverified Information

None identified.

### AI Analysis
> Model: N/A | Analyzed: 2026-05-10 01:32 UTC

AI analysis was skipped because --no-ai was used.

### Command Outputs

Command: `nmap -sT -T4 --top-ports 1000 127.0.0.1`
```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-09 21:28 -0400
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000032s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT      STATE SERVICE
3306/tcp  open  mysql
5000/tcp  open  upnp
7000/tcp  open  afs3-fileserver
28201/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 0.03 seconds
```

Command: `nmap -sT -sV -sC -p- 127.0.0.1`
```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-09 21:28 -0400
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000021s latency).
Not shown: 65525 closed tcp ports (conn-refused)
PORT      STATE    SERVICE        VERSION
3306/tcp  open     mysql?
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     9.4.0
|     ?;je
|     4Vxj
|     UvA]
|     caching_sha2_password
|     #08S01Got packets out of order
|   DNSVersionBindReqTCP: 
|     9.4.0
|     3ry+MQsZu%M
|     caching_sha2_password
|     #08S01Got packets out of order
|   GenericLines: 
|     9.4.0
|     X2{h
|     (!#]
|     caching_sha2_password
|     #08S01Got packets out of order
|   GetRequest: 
|     9.4.0
|     OR!/l
|     )P%7>B
|     caching_sha2_password
|     #08S01Got packets out of order
|   HTTPOptions: 
|     9.4.0
|     FYTRqRD
|     mL>>^
|     caching_sha2_password
|     #08S01Got packets out of order
|   Help: 
|     9.4.0
|     K^Ay
|     uM@c{
|     caching_sha2_password
|     #08S01Got packets out of order
|   NULL: 
|     9.4.0
|     X2{h
|     (!#]
|     caching_sha2_password
|   RPCCheck: 
|     9.4.0
|     >fy%
|     _&x}f
|     caching_sha2_password
|     #08S01Got packets out of order
|   RTSPRequest: 
|     9.4.0
|     Ow")WO
|     dA%Z t
|     caching_sha2_password
|     #08S01Got packets out of order
|   SSLSessionReq: 
|     9.4.0
|     Opm,ySiNHkF
|     caching_sha2_password
|_    #08S01Got packets out of order
| mysql-info: 
|   Protocol: 10
|   Version: 9.4.0
|   Thread ID: 42
|   Capabilities flags: 65535
|   Some Capabilities: SupportsCompression, Speaks41ProtocolOld, Speaks41ProtocolNew, IgnoreSigpipes, LongColumnFlag, SupportsTransactions, FoundRows, IgnoreSpaceBeforeParenthesis, Support41Auth, ConnectWithDatabase, SwitchToSSLAfterHandshake, ODBCClient, SupportsLoadDataLocal, LongPassword, DontAllowDatabaseTableColumn, InteractiveClient, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: X'ZpYw38\x19&	\x13\x02^%)>2x\x1B
|_  Auth Plugin Name: caching_sha2_password
| ssl-cert: Subject: commonName=MySQL_Server_9.4.0_Auto_Generated_Server_Certificate
| Not valid before: 2025-09-03T17:01:00
|_Not valid after:  2035-09-01T17:01:00
|_ssl-date: TLS randomness does not represent time
5000/tcp  open     rtsp
|_rtsp-methods: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110643630
|   GetRequest: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110638616
|   HTTPOptions: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110643629
|   RTSPRequest: 
|     RTSP/1.0 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110638628
|   SIPOptions: 
|     RTSP/1.0 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     CSeq: 42 OPTIONS
|     X-Apple-ProcessingTime: 0
|_    X-Apple-RequestReceivedTimestamp: 110643632
7000/tcp  open     rtsp
|_rtsp-methods: ERROR: Script execution failed (use -d to debug)
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110643626
|   GetRequest: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110643618
|   HTTPOptions: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110643624
|   RTSPRequest: 
|     RTSP/1.0 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 1
|     X-Apple-RequestReceivedTimestamp: 110638614
|   SIPOptions: 
|     RTSP/1.0 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     CSeq: 42 OPTIONS
|     X-Apple-ProcessingTime: 0
|_    X-Apple-RequestReceivedTimestamp: 110643628
|_irc-info: Unable to open connection
28201/tcp open     pharos         Pharos Notify (printing client)
33060/tcp open     mysqlx         MySQL X protocol listener
49344/tcp open     unknown
50327/tcp open     unknown
56761/tcp open     bandwidth-test MikroTik bandwidth-test server
62654/tcp filtered unknown
63342/tcp open     http           PyCharm 2025.1.2
|_http-server-header: PyCharm 2025.1.2
|_http-title: 404 Not Found
3 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3306-TCP:V=7.99%I=7%D=5/9%Time=69FFDF60%P=arm-apple-darwin24.6.0%r(
SF:NULL,4D,"I\0\0\0\n9\.4\.0\0\x0c\0\0\0\x04GZ\x0bW24\x18\0\xff\xff\xff\x0
SF:2\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0X2{h\x1fWO\t\(!#\]\0caching_sha2_pas
SF:sword\0")%r(GenericLines,72,"I\0\0\0\n9\.4\.0\0\x0c\0\0\0\x04GZ\x0bW24\
SF:x18\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0X2{h\x1fWO\t\(!#
SF:\]\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x2
SF:0out\x20of\x20order")%r(GetRequest,72,"I\0\0\0\n9\.4\.0\0\x0e\0\0\0OR!/
SF:l\r5U\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0\x11\x01\n\)P%
SF:7>B\x04\x19`\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20
SF:packets\x20out\x20of\x20order")%r(HTTPOptions,72,"I\0\0\0\n9\.4\.0\0\x0
SF:f\0\0\0FYTRqRD\x08\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0\
SF:x0b\nAb\^\x7fmL>>\^\x19\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#0
SF:8S01Got\x20packets\x20out\x20of\x20order")%r(RTSPRequest,72,"I\0\0\0\n9
SF:\.4\.0\0\x10\0\0\0~\x0eOw\"\)WO\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0
SF:\0\0\0\0\0\0Fsv\x16g\x16dA%Z\x20t\0caching_sha2_password\0!\0\0\x01\xff
SF:\x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%r(RPCCheck,72,"I\0
SF:\0\0\n9\.4\.0\0\x11\0\0\0>fy%\x16\]fx\0\xff\xff\xff\x02\0\xff\xdf\x15\0
SF:\0\0\0\0\0\0\0\0\0,HP\r_&x}f\x01XA\0caching_sha2_password\0!\0\0\x01\xf
SF:f\x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%r(DNSVersionBindR
SF:eqTCP,72,"I\0\0\0\n9\.4\.0\0\x12\0\0\0z#8\x04\(#Y\x1b\0\xff\xff\xff\x02
SF:\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\x003ry\+MQ\\sZu%M\0caching_sha2_passwo
SF:rd\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%r
SF:(DNSStatusRequestTCP,72,"I\0\0\0\n9\.4\.0\0\x13\0\0\0Y\x02\x0b\?;je\x05
SF:\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\x004Vxj\x06UvA\]\x11
SF:jr\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x2
SF:0out\x20of\x20order")%r(Help,72,"I\0\0\0\n9\.4\.0\0\x14\0\0\0\x0byZ\x1a
SF:K\^Ay\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0_\x12\x1d<\x1c
SF:\x0euM@c{\x7f\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x2
SF:0packets\x20out\x20of\x20order")%r(SSLSessionReq,72,"I\0\0\0\n9\.4\.0\0
SF:\x15\0\0\0e;\x1d,IS\x13\x01\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0
SF:\0\0\0\0Opm,ySiNHkF\x19\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#0
SF:8S01Got\x20packets\x20out\x20of\x20order");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5000-TCP:V=7.99%I=7%D=5/9%Time=69FFDF60%P=arm-apple-darwin24.6.0%r(
SF:GetRequest,90,"HTTP/1\.1\x20403\x20Forbidden\r\nContent-Length:\x200\r\
SF:nServer:\x20AirTunes/870\.14\.1\r\nX-Apple-ProcessingTime:\x200\r\nX-Ap
SF:ple-RequestReceivedTimestamp:\x20110638616\r\n\r\n")%r(RTSPRequest,90,"
SF:RTSP/1\.0\x20403\x20Forbidden\r\nContent-Length:\x200\r\nServer:\x20Air
SF:Tunes/870\.14\.1\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestRece
SF:ivedTimestamp:\x20110638628\r\n\r\n")%r(HTTPOptions,90,"HTTP/1\.1\x2040
SF:3\x20Forbidden\r\nContent-Length:\x200\r\nServer:\x20AirTunes/870\.14\.
SF:1\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:\
SF:x20110643629\r\n\r\n")%r(FourOhFourRequest,90,"HTTP/1\.1\x20403\x20Forb
SF:idden\r\nContent-Length:\x200\r\nServer:\x20AirTunes/870\.14\.1\r\nX-Ap
SF:ple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:\x20110643
SF:630\r\n\r\n")%r(SIPOptions,A2,"RTSP/1\.0\x20403\x20Forbidden\r\nContent
SF:-Length:\x200\r\nServer:\x20AirTunes/870\.14\.1\r\nCSeq:\x2042\x20OPTIO
SF:NS\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:
SF:\x20110643632\r\n\r\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port7000-TCP:V=7.99%I=7%D=5/9%Time=69FFDF65%P=arm-apple-darwin24.6.0%r(
SF:RTSPRequest,90,"RTSP/1\.0\x20403\x20Forbidden\r\nContent-Length:\x200\r
SF:\nServer:\x20AirTunes/870\.14\.1\r\nX-Apple-ProcessingTime:\x201\r\nX-A
SF:pple-RequestReceivedTimestamp:\x20110638614\r\n\r\n")%r(GetRequest,90,"
SF:HTTP/1\.1\x20403\x20Forbidden\r\nContent-Length:\x200\r\nServer:\x20Air
SF:Tunes/870\.14\.1\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestRece
SF:ivedTimestamp:\x20110643618\r\n\r\n")%r(HTTPOptions,90,"HTTP/1\.1\x2040
SF:3\x20Forbidden\r\nContent-Length:\x200\r\nServer:\x20AirTunes/870\.14\.
SF:1\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:\
SF:x20110643624\r\n\r\n")%r(FourOhFourRequest,90,"HTTP/1\.1\x20403\x20Forb
SF:idden\r\nContent-Length:\x200\r\nServer:\x20AirTunes/870\.14\.1\r\nX-Ap
SF:ple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:\x20110643
SF:626\r\n\r\n")%r(SIPOptions,A2,"RTSP/1\.0\x20403\x20Forbidden\r\nContent
SF:-Length:\x200\r\nServer:\x20AirTunes/870\.14\.1\r\nCSeq:\x2042\x20OPTIO
SF:NS\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:
SF:\x20110643628\r\n\r\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 215.38 seconds

[stderr]
Strange read error from 127.0.0.1 (22 - 'Invalid argument')
```

Command: `nmap -O 127.0.0.1`
```

[stderr]
TCP/IP fingerprinting (for OS scan) requires root privileges.
QUITTING!
```

---
