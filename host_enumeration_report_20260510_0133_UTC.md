# Host Enumeration Report

Generated: 2026-05-10 01:36 UTC

---

## Host: 127.0.0.1

### Verified Information

| Field | Value |
|---|---|
| IP Address | 127.0.0.1 |
| Hostname | localhost |
| Domain | Unknown |
| Operating System | Unknown |
| Active Services | mysql (3306/tcp) - 5000/tcp  open  upnp<br>afs3-fileserver (7000/tcp) - 28201/tcp open  unknown<br>rtsp (5000/tcp) - | fingerprint-strings:<br>pharos (28201/tcp) - Pharos Notify (printing client)<br>mysqlx (33060/tcp) - MySQL X protocol listener<br>unknown (49344/tcp) - 49850/tcp filtered unknown<br>unknown (50327/tcp) - 55380/tcp filtered unknown<br>bandwidth-test (56761/tcp) - MikroTik bandwidth-test server<br>http (63342/tcp) - PyCharm 2025.1.2 |
| Windows-Specific Information | None detected |

### Unverified Information

None identified.

### AI Analysis
> Model: gemma4:e4b | Analyzed: 2026-05-10 01:36 UTC

AI analysis was skipped because Ollama was unavailable.

### Command Outputs

Command: `nmap -sT -T4 --top-ports 1000 127.0.0.1`
```
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-09 21:33 -0400
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000022s latency).
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
Starting Nmap 7.99 ( https://nmap.org ) at 2026-05-09 21:33 -0400
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000025s latency).
Not shown: 65524 closed tcp ports (conn-refused)
PORT      STATE    SERVICE        VERSION
3306/tcp  open     mysql?
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     9.4.0
|     _{l%[
|     'C7g=@Fht
|     caching_sha2_password
|     #08S01Got packets out of order
|   DNSVersionBindReqTCP: 
|     9.4.0
|     8nim
|     v^30uU
|     caching_sha2_password
|     #08S01Got packets out of order
|   GenericLines: 
|     9.4.0
|     <6?k)
|     uM&;
|     caching_sha2_password
|     #08S01Got packets out of order
|   GetRequest: 
|     9.4.0
|     V5~'
|     OQT<>@^M 1h
|     caching_sha2_password
|     #08S01Got packets out of order
|   HTTPOptions: 
|     9.4.0
|     {?4?
|     tPCYKZJ"j6*
|     caching_sha2_password
|     #08S01Got packets out of order
|   Help: 
|     9.4.0
|     avQYo
|     caching_sha2_password
|     #08S01Got packets out of order
|   NULL: 
|     9.4.0
|     <6?k)
|     uM&;
|     caching_sha2_password
|   RPCCheck: 
|     9.4.0
|     P%Dxc92
|     caching_sha2_password
|     #08S01Got packets out of order
|   RTSPRequest: 
|     9.4.0
|     1I'u`
|     caching_sha2_password
|     #08S01Got packets out of order
|   SSLSessionReq: 
|     9.4.0
|     8[No8
|     8fN5&
|     S~u%
|     caching_sha2_password
|_    #08S01Got packets out of order
| mysql-info: 
|   Protocol: 10
|   Version: 9.4.0
|   Thread ID: 85
|   Capabilities flags: 65535
|   Some Capabilities: FoundRows, Support41Auth, SupportsTransactions, Speaks41ProtocolOld, IgnoreSigpipes, SwitchToSSLAfterHandshake, Speaks41ProtocolNew, SupportsLoadDataLocal, SupportsCompression, InteractiveClient, DontAllowDatabaseTableColumn, ConnectWithDatabase, LongPassword, LongColumnFlag, ODBCClient, IgnoreSpaceBeforeParenthesis, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: *\x1C\x1D\x01l\x11\x03#%BH*t9\x11\x04t&MS
|_  Auth Plugin Name: caching_sha2_password
| ssl-cert: Subject: commonName=MySQL_Server_9.4.0_Auto_Generated_Server_Certificate
| Not valid before: 2025-09-03T17:01:00
|_Not valid after:  2035-09-01T17:01:00
|_ssl-date: TLS randomness does not represent time
5000/tcp  open     rtsp
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110895885
|   GetRequest: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110890877
|   HTTPOptions: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110895882
|   RTSPRequest: 
|     RTSP/1.0 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110890882
|   SIPOptions: 
|     RTSP/1.0 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     CSeq: 42 OPTIONS
|     X-Apple-ProcessingTime: 0
|_    X-Apple-RequestReceivedTimestamp: 110895887
|_rtsp-methods: ERROR: Script execution failed (use -d to debug)
7000/tcp  open     rtsp
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110895880
|   GetRequest: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110895873
|   HTTPOptions: 
|     HTTP/1.1 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110895879
|   RTSPRequest: 
|     RTSP/1.0 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     X-Apple-ProcessingTime: 0
|     X-Apple-RequestReceivedTimestamp: 110890870
|   SIPOptions: 
|     RTSP/1.0 403 Forbidden
|     Content-Length: 0
|     Server: AirTunes/870.14.1
|     CSeq: 42 OPTIONS
|     X-Apple-ProcessingTime: 0
|_    X-Apple-RequestReceivedTimestamp: 110895882
|_irc-info: Unable to open connection
|_rtsp-methods: ERROR: Script execution failed (use -d to debug)
28201/tcp open     pharos         Pharos Notify (printing client)
33060/tcp open     mysqlx         MySQL X protocol listener
49344/tcp open     unknown
49850/tcp filtered unknown
50327/tcp open     unknown
55380/tcp filtered unknown
56761/tcp open     bandwidth-test MikroTik bandwidth-test server
63342/tcp open     http           PyCharm 2025.1.2
|_http-title: 404 Not Found
|_http-server-header: PyCharm 2025.1.2
3 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3306-TCP:V=7.99%I=7%D=5/9%Time=69FFE05C%P=arm-apple-darwin24.6.0%r(
SF:NULL,4D,"I\0\0\0\n9\.4\.0\x007\0\0\0<6\?k\)\x1a,4\0\xff\xff\xff\x02\0\x
SF:ff\xdf\x15\0\0\0\0\0\0\0\0\0\0\x03uM&;\x01o\x01\x0c\x0f~0\0caching_sha2
SF:_password\0")%r(GenericLines,72,"I\0\0\0\n9\.4\.0\x007\0\0\0<6\?k\)\x1a
SF:,4\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0\x03uM&;\x01o\x01
SF:\x0c\x0f~0\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20pa
SF:ckets\x20out\x20of\x20order")%r(GetRequest,72,"I\0\0\0\n9\.4\.0\x009\0\
SF:0\0=\x11\n\x02V5~'\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0\
SF:x15OQT<>@\^M\t1h\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got
SF:\x20packets\x20out\x20of\x20order")%r(HTTPOptions,72,"I\0\0\0\n9\.4\.0\
SF:0:\0\0\0{\?4\?\x07:}`\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0
SF:\0\x1atPCYKZJ\"j6\*\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01
SF:Got\x20packets\x20out\x20of\x20order")%r(RTSPRequest,72,"I\0\0\0\n9\.4\
SF:.0\0;\0\0\0H\x1f\x181I'u`\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0
SF:\0\0\x006p3\x13~hn\x03\x16J\x0e>\0caching_sha2_password\0!\0\0\x01\xff\
SF:x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%r(RPCCheck,72,"I\0\
SF:0\0\n9\.4\.0\0<\0\0\0\x03\\\+\x20A\x11=C\0\xff\xff\xff\x02\0\xff\xdf\x1
SF:5\0\0\0\0\0\0\0\0\0\0P%Dxc92\x044\x1cLx\0caching_sha2_password\0!\0\0\x
SF:01\xff\x84\x04#08S01Got\x20packets\x20out\x20of\x20order")%r(DNSVersion
SF:BindReqTCP,72,"I\0\0\0\n9\.4\.0\0=\0\0\0\.j\x0f\x178nim\0\xff\xff\xff\x
SF:02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0>b\x16S\?\x13v\^30uU\0caching_sha2_
SF:password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out\x20of\x20ord
SF:er")%r(DNSStatusRequestTCP,72,"I\0\0\0\n9\.4\.0\0>\0\0\0_{l%\[\x06s}\0\
SF:xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0'C7g=@Fht\x11%\x13\0ca
SF:ching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x20out\x
SF:20of\x20order")%r(Help,72,"I\0\0\0\n9\.4\.0\0\?\0\0\0\x17N\x19\x20\x0e{
SF:5g\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\0avQYo\x07\x10&Vs\
SF:rg\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\x20packets\x2
SF:0out\x20of\x20order")%r(SSLSessionReq,72,"I\0\0\0\n9\.4\.0\0@\0\0\0\x07
SF:\x038\[No8\x17\0\xff\xff\xff\x02\0\xff\xdf\x15\0\0\0\0\0\0\0\0\0\x008fN
SF:5&\x1dQ\x08S~u%\0caching_sha2_password\0!\0\0\x01\xff\x84\x04#08S01Got\
SF:x20packets\x20out\x20of\x20order");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5000-TCP:V=7.99%I=7%D=5/9%Time=69FFE05C%P=arm-apple-darwin24.6.0%r(
SF:GetRequest,90,"HTTP/1\.1\x20403\x20Forbidden\r\nContent-Length:\x200\r\
SF:nServer:\x20AirTunes/870\.14\.1\r\nX-Apple-ProcessingTime:\x200\r\nX-Ap
SF:ple-RequestReceivedTimestamp:\x20110890877\r\n\r\n")%r(RTSPRequest,90,"
SF:RTSP/1\.0\x20403\x20Forbidden\r\nContent-Length:\x200\r\nServer:\x20Air
SF:Tunes/870\.14\.1\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestRece
SF:ivedTimestamp:\x20110890882\r\n\r\n")%r(HTTPOptions,90,"HTTP/1\.1\x2040
SF:3\x20Forbidden\r\nContent-Length:\x200\r\nServer:\x20AirTunes/870\.14\.
SF:1\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:\
SF:x20110895882\r\n\r\n")%r(FourOhFourRequest,90,"HTTP/1\.1\x20403\x20Forb
SF:idden\r\nContent-Length:\x200\r\nServer:\x20AirTunes/870\.14\.1\r\nX-Ap
SF:ple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:\x20110895
SF:885\r\n\r\n")%r(SIPOptions,A2,"RTSP/1\.0\x20403\x20Forbidden\r\nContent
SF:-Length:\x200\r\nServer:\x20AirTunes/870\.14\.1\r\nCSeq:\x2042\x20OPTIO
SF:NS\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:
SF:\x20110895887\r\n\r\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port7000-TCP:V=7.99%I=7%D=5/9%Time=69FFE061%P=arm-apple-darwin24.6.0%r(
SF:RTSPRequest,90,"RTSP/1\.0\x20403\x20Forbidden\r\nContent-Length:\x200\r
SF:\nServer:\x20AirTunes/870\.14\.1\r\nX-Apple-ProcessingTime:\x200\r\nX-A
SF:pple-RequestReceivedTimestamp:\x20110890870\r\n\r\n")%r(GetRequest,90,"
SF:HTTP/1\.1\x20403\x20Forbidden\r\nContent-Length:\x200\r\nServer:\x20Air
SF:Tunes/870\.14\.1\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestRece
SF:ivedTimestamp:\x20110895873\r\n\r\n")%r(HTTPOptions,90,"HTTP/1\.1\x2040
SF:3\x20Forbidden\r\nContent-Length:\x200\r\nServer:\x20AirTunes/870\.14\.
SF:1\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:\
SF:x20110895879\r\n\r\n")%r(FourOhFourRequest,90,"HTTP/1\.1\x20403\x20Forb
SF:idden\r\nContent-Length:\x200\r\nServer:\x20AirTunes/870\.14\.1\r\nX-Ap
SF:ple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:\x20110895
SF:880\r\n\r\n")%r(SIPOptions,A2,"RTSP/1\.0\x20403\x20Forbidden\r\nContent
SF:-Length:\x200\r\nServer:\x20AirTunes/870\.14\.1\r\nCSeq:\x2042\x20OPTIO
SF:NS\r\nX-Apple-ProcessingTime:\x200\r\nX-Apple-RequestReceivedTimestamp:
SF:\x20110895882\r\n\r\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 215.25 seconds

[stderr]
Strange read error from 127.0.0.1 (22 - 'Invalid argument')
Strange read error from 127.0.0.1 (22 - 'Invalid argument')
```

Command: `nmap -O 127.0.0.1`
```

[stderr]
TCP/IP fingerprinting (for OS scan) requires root privileges.
QUITTING!
```

---
