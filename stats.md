OpenCL Platform #1: NVIDIA Corporation
======================================
* Device #1: Tesla V100-SXM2-16GB, 4032/16130 MB allocatable, 80MCU

Benchmark relevant options:
===========================
* --benchmark-all
* --optimized-kernel-enable

Hashmode: 0 - MD5

Speed.#1.........: 55214.9 MH/s (48.11ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 10 - md5($pass.$salt)

Speed.#1.........: 55307.6 MH/s (48.13ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 11 - Joomla < 2.5.18

Speed.#1.........: 55309.2 MH/s (48.13ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 12 - PostgreSQL

Speed.#1.........: 55312.0 MH/s (48.13ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 20 - md5($salt.$pass)

Speed.#1.........: 29901.7 MH/s (88.92ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 21 - osCommerce, xt:Commerce

Speed.#1.........: 29908.5 MH/s (88.90ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 22 - Juniper NetScreen/SSG (ScreenOS)

Speed.#1.........: 29665.8 MH/s (89.64ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 23 - Skype

Speed.#1.........: 29913.9 MH/s (88.89ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 30 - md5(utf16le($pass).$salt)

Speed.#1.........: 53949.6 MH/s (48.52ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 40 - md5($salt.utf16le($pass))

Speed.#1.........: 29965.5 MH/s (88.87ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 50 - HMAC-MD5 (key = $pass)

Speed.#1.........:  8708.9 MH/s (76.31ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 60 - HMAC-MD5 (key = $salt)

Speed.#1.........: 18262.0 MH/s (72.78ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 100 - SHA1

Speed.#1.........: 17059.6 MH/s (77.91ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 101 - nsldap, SHA-1(Base64), Netscape LDAP SHA

Speed.#1.........: 17064.4 MH/s (77.89ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 110 - sha1($pass.$salt)

Speed.#1.........: 17103.6 MH/s (77.89ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 111 - nsldaps, SSHA-1(Base64), Netscape LDAP SSHA

Speed.#1.........: 17098.6 MH/s (77.90ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 112 - Oracle S: Type (Oracle 11+)

Speed.#1.........: 17104.3 MH/s (77.90ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 120 - sha1($salt.$pass)

Speed.#1.........: 12390.1 MH/s (53.61ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 121 - SMF (Simple Machines Forum) > v1.1

Speed.#1.........: 12392.6 MH/s (53.60ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 122 - macOS v10.4, macOS v10.5, MacOS v10.6

Speed.#1.........: 12393.4 MH/s (53.60ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 124 - Django (SHA-1)

Speed.#1.........: 12388.7 MH/s (53.62ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 125 - ArubaOS

Speed.#1.........: 12388.5 MH/s (53.61ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 130 - sha1(utf16le($pass).$salt)

Speed.#1.........: 17397.9 MH/s (76.17ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 131 - MSSQL (2000)

Speed.#1.........: 17399.1 MH/s (76.17ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 132 - MSSQL (2005)

Speed.#1.........: 17403.1 MH/s (76.15ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 133 - PeopleSoft

Speed.#1.........: 17409.8 MH/s (76.13ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 140 - sha1($salt.utf16le($pass))

Speed.#1.........: 12413.6 MH/s (53.61ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 141 - Episerver 6.x < .NET 4

Speed.#1.........: 12410.9 MH/s (53.61ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 150 - HMAC-SHA1 (key = $pass)

Speed.#1.........:  3564.7 MH/s (93.24ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 160 - HMAC-SHA1 (key = $salt)

Speed.#1.........:  6587.8 MH/s (50.41ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 200 - MySQL323

Speed.#1.........:   170.5 GH/s (15.56ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 300 - MySQL4.1/MySQL5

Speed.#1.........:  7462.7 MH/s (89.09ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 400 - phpass, WordPress (MD5), phpBB3 (MD5), Joomla (MD5) (Iterations: 2048)

Speed.#1.........: 12962.6 kH/s (84.31ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 500 - md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5) (Iterations: 1000)

Speed.#1.........: 19219.3 kH/s (50.81ms) @ Accel:1024 Loops:500 Thr:32 Vec:1

Hashmode: 501 - Juniper IVE (Iterations: 1000)

Speed.#1.........: 19087.3 kH/s (50.81ms) @ Accel:1024 Loops:500 Thr:32 Vec:1

Hashmode: 600 - BLAKE2b

Speed.#1.........:  4029.7 MH/s (82.48ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 900 - MD4

Speed.#1.........: 81435.9 MH/s (32.59ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 1000 - NTLM

Speed.#1.........: 77681.7 MH/s (34.00ms) @ Accel:128 Loops:1024 Thr:256 Vec:2

Hashmode: 1100 - Domain Cached Credentials (DCC), MS Cache

Speed.#1.........: 22261.7 MH/s (59.80ms) @ Accel:128 Loops:512 Thr:256 Vec:4

Hashmode: 1300 - SHA2-224

Speed.#1.........:  7410.3 MH/s (89.69ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1400 - SHA2-256

Speed.#1.........:  7613.2 MH/s (87.30ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1410 - sha256($pass.$salt)

Speed.#1.........:  7630.5 MH/s (87.32ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1411 - SSHA-256(Base64), LDAP {SSHA256}

Speed.#1.........:  7630.7 MH/s (87.31ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1420 - sha256($salt.$pass)

Speed.#1.........:  6691.9 MH/s (49.62ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 1421 - hMailServer

Speed.#1.........:  6692.5 MH/s (49.62ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 1430 - sha256(utf16le($pass).$salt)

Speed.#1.........:  7521.5 MH/s (88.11ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1440 - sha256($salt.utf16le($pass))

Speed.#1.........:  6706.9 MH/s (49.62ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 1441 - Episerver 6.x >= .NET 4

Speed.#1.........:  6705.6 MH/s (49.62ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 1450 - HMAC-SHA256 (key = $pass)

Speed.#1.........:  1206.8 MH/s (68.84ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 1460 - HMAC-SHA256 (key = $salt)

Speed.#1.........:  2736.3 MH/s (60.70ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1500 - descrypt, DES (Unix), Traditional DES

Speed.#1.........:  1814.9 MH/s (92.23ms) @ Accel:8 Loops:1024 Thr:256 Vec:1

Hashmode: 1600 - Apache $apr1$ MD5, md5apr1, MD5 (APR) (Iterations: 1000)

Speed.#1.........: 19241.8 kH/s (50.83ms) @ Accel:1024 Loops:500 Thr:32 Vec:1

Hashmode: 1700 - SHA2-512

Speed.#1.........:  2337.6 MH/s (71.07ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1710 - sha512($pass.$salt)

Speed.#1.........:  2343.0 MH/s (71.07ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1711 - SSHA-512(Base64), LDAP {SSHA512}

Speed.#1.........:  2342.8 MH/s (71.08ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1720 - sha512($salt.$pass)

Speed.#1.........:  2184.5 MH/s (76.06ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1722 - macOS v10.7

Speed.#1.........:  2184.8 MH/s (76.05ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1730 - sha512(utf16le($pass).$salt)

Speed.#1.........:  2336.2 MH/s (70.92ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1731 - MSSQL (2012, 2014)

Speed.#1.........:  2338.7 MH/s (70.94ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1740 - sha512($salt.utf16le($pass))

Speed.#1.........:  2225.8 MH/s (74.78ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1750 - HMAC-SHA512 (key = $pass)

Speed.#1.........:   444.9 MH/s (46.84ms) @ Accel:64 Loops:16 Thr:256 Vec:1

Hashmode: 1760 - HMAC-SHA512 (key = $salt)

Speed.#1.........:   917.6 MH/s (90.55ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 1800 - sha512crypt $6$, SHA512 (Unix) (Iterations: 5000)

Speed.#1.........:   374.4 kH/s (86.21ms) @ Accel:512 Loops:128 Thr:32 Vec:1

Hashmode: 2100 - Domain Cached Credentials 2 (DCC2), MS Cache 2 (Iterations: 10240)

Speed.#1.........:   656.6 kH/s (49.42ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 2400 - Cisco-PIX MD5

Speed.#1.........: 39543.7 MH/s (67.21ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 2410 - Cisco-ASA MD5

Speed.#1.........: 41173.1 MH/s (64.54ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 2500 - WPA-EAPOL-PBKDF2 (Iterations: 4096)

Speed.#1.........:   808.1 kH/s (49.96ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 2501 - WPA-EAPOL-PMK (Iterations: 1)

Speed.#1.........: 56695.6 kH/s (0.02ms) @ Accel:128 Loops:1 Thr:256 Vec:1

Hashmode: 2600 - md5(md5($pass))

Speed.#1.........: 15668.2 MH/s (84.85ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 2611 - vBulletin < v3.8.5

Speed.#1.........: 15669.8 MH/s (84.83ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 2612 - PHPS

Speed.#1.........: 15666.7 MH/s (84.85ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 2711 - vBulletin >= v3.8.5

Speed.#1.........: 11105.9 MH/s (59.82ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 2811 - IPB2+ (Invision Power Board), MyBB 1.2+

Speed.#1.........: 11662.4 MH/s (56.97ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 3000 - LM

Speed.#1.........: 45353.4 MH/s (58.53ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 3100 - Oracle H: Type (Oracle 7+)

Speed.#1.........:  2418.5 MH/s (68.69ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 3200 - bcrypt $2*$, Blowfish (Unix) (Iterations: 32)

Speed.#1.........:    54216 H/s (46.07ms) @ Accel:16 Loops:8 Thr:8 Vec:1

Hashmode: 3710 - md5($salt.md5($pass))

Speed.#1.........: 14928.7 MH/s (89.04ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 3711 - MediaWiki B type

Speed.#1.........: 14927.1 MH/s (89.05ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 3800 - md5($salt.$pass.$salt)

Speed.#1.........: 30002.4 MH/s (88.61ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 3910 - md5(md5($pass).md5($salt))

Speed.#1.........: 11122.9 MH/s (59.73ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 4010 - md5($salt.md5($salt.$pass))

Speed.#1.........: 11939.3 MH/s (55.64ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 4110 - md5($salt.md5($pass.$salt))

Speed.#1.........: 12626.7 MH/s (52.61ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 4300 - md5(strtoupper(md5($pass)))

Speed.#1.........: 15665.9 MH/s (84.84ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 4400 - md5(sha1($pass))

Speed.#1.........:  9376.0 MH/s (70.87ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 4500 - sha1(sha1($pass))

Speed.#1.........:  6616.6 MH/s (50.18ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 4520 - sha1($salt.sha1($pass))

Speed.#1.........:  5692.0 MH/s (58.35ms) @ Accel:128 Loops:128 Thr:256 Vec:2

Hashmode: 4521 - Redmine

Speed.#1.........:  5693.8 MH/s (58.34ms) @ Accel:128 Loops:128 Thr:256 Vec:2

Hashmode: 4522 - PunBB

Speed.#1.........:  5692.4 MH/s (58.35ms) @ Accel:128 Loops:128 Thr:256 Vec:2

Hashmode: 4700 - sha1(md5($pass))

Speed.#1.........:  9625.2 MH/s (69.03ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 4800 - iSCSI CHAP authentication, MD5(CHAP)

Speed.#1.........: 32596.6 MH/s (81.56ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 4900 - sha1($salt.$pass.$salt)

Speed.#1.........: 12044.8 MH/s (55.15ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 5100 - Half MD5

Speed.#1.........: 34483.9 MH/s (77.10ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 5200 - Password Safe v3 (Iterations: 2048)

Speed.#1.........:  2900.7 kH/s (54.28ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 5300 - IKE-PSK MD5

Speed.#1.........:  4244.5 MH/s (78.29ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 5400 - IKE-PSK SHA1

Speed.#1.........:  1475.3 MH/s (56.29ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 5500 - NetNTLMv1 / NetNTLMv1+ESS

Speed.#1.........: 44143.7 MH/s (59.87ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 5600 - NetNTLMv2

Speed.#1.........:  3806.9 MH/s (87.45ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 5700 - Cisco-IOS type 4 (SHA256)

Speed.#1.........:  7611.9 MH/s (87.32ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 5800 - Samsung Android Password/PIN (Iterations: 1023)

Speed.#1.........: 10406.4 kH/s (43.38ms) @ Accel:128 Loops:255 Thr:256 Vec:1

Hashmode: 6000 - RIPEMD-160

Speed.#1.........:  9910.0 MH/s (67.06ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 6100 - Whirlpool

Speed.#1.........:   780.2 MH/s (53.44ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 6211 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 512 bit (Iterations: 2000)

Speed.#1.........:   620.6 kH/s (66.28ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 6212 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1024 bit (Iterations: 2000)

Speed.#1.........:   213.0 kH/s (59.18ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 6213 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1536 bit (Iterations: 2000)

Speed.#1.........:   240.7 kH/s (84.49ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 6221 - TrueCrypt PBKDF2-HMAC-SHA512 + XTS 512 bit (Iterations: 1000)

Speed.#1.........:   754.9 kH/s (81.13ms) @ Accel:64 Loops:62 Thr:256 Vec:1

Hashmode: 6222 - TrueCrypt PBKDF2-HMAC-SHA512 + XTS 1024 bit (Iterations: 1000)

Speed.#1.........:   270.5 kH/s (75.05ms) @ Accel:64 Loops:31 Thr:256 Vec:1

Hashmode: 6223 - TrueCrypt PBKDF2-HMAC-SHA512 + XTS 1536 bit (Iterations: 1000)

Speed.#1.........:   190.8 kH/s (56.77ms) @ Accel:32 Loops:31 Thr:256 Vec:1

Hashmode: 6231 - TrueCrypt PBKDF2-HMAC-Whirlpool + XTS 512 bit (Iterations: 1000)

Speed.#1.........:   119.1 kH/s (169.84ms) @ Accel:32 Loops:31 Thr:256 Vec:1

Hashmode: 6232 - TrueCrypt PBKDF2-HMAC-Whirlpool + XTS 1024 bit (Iterations: 1000)

Speed.#1.........:    58866 H/s (166.05ms) @ Accel:32 Loops:15 Thr:256 Vec:1

Hashmode: 6233 - TrueCrypt PBKDF2-HMAC-Whirlpool + XTS 1536 bit (Iterations: 1000)

Speed.#1.........:    39164 H/s (125.07ms) @ Accel:16 Loops:15 Thr:256 Vec:1

Hashmode: 6241 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 512 bit + boot-mode (Iterations: 1000)

Speed.#1.........:   936.2 kH/s (60.60ms) @ Accel:64 Loops:62 Thr:256 Vec:1

Hashmode: 6242 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1024 bit + boot-mode (Iterations: 1000)

Speed.#1.........:   304.4 kH/s (56.49ms) @ Accel:64 Loops:31 Thr:256 Vec:1

Hashmode: 6243 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1536 bit + boot-mode (Iterations: 1000)

Speed.#1.........:   223.3 kH/s (80.76ms) @ Accel:64 Loops:31 Thr:256 Vec:1

Hashmode: 6300 - AIX {smd5} (Iterations: 1000)

Speed.#1.........: 19209.1 kH/s (51.00ms) @ Accel:1024 Loops:500 Thr:32 Vec:1

Hashmode: 6400 - AIX {ssha256} (Iterations: 64)

Speed.#1.........: 27642.6 kH/s (57.44ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 6500 - AIX {ssha512} (Iterations: 64)

Speed.#1.........: 11771.3 kH/s (88.21ms) @ Accel:64 Loops:64 Thr:256 Vec:1

Hashmode: 6600 - 1Password, agilekeychain (Iterations: 1000)

Speed.#1.........:  6026.6 kH/s (49.24ms) @ Accel:128 Loops:125 Thr:256 Vec:1

Hashmode: 6700 - AIX {ssha1} (Iterations: 64)

Speed.#1.........: 42790.8 kH/s (25.21ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 6800 - LastPass + LastPass sniffed (Iterations: 500)

Speed.#1.........:  5275.9 kH/s (49.97ms) @ Accel:128 Loops:62 Thr:256 Vec:1

Hashmode: 6900 - GOST R 34.11-94

Speed.#1.........:   733.9 MH/s (56.81ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 7000 - FortiGate (FortiOS)

Speed.#1.........: 13741.6 MH/s (96.75ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 7100 - macOS v10.8+ (PBKDF2-SHA512) (Iterations: 35000)

Speed.#1.........:    26857 H/s (88.18ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 7200 - GRUB 2 (Iterations: 10000)

Speed.#1.........:    93958 H/s (88.20ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 7300 - IPMI2 RAKP HMAC-SHA1

Speed.#1.........:  3079.0 MH/s (53.93ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 7400 - sha256crypt $5$, SHA256 (Unix) (Iterations: 5000)

Speed.#1.........:  1037.7 kH/s (61.71ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 7500 - Kerberos 5 AS-REQ Pre-Auth etype 23

Speed.#1.........:   999.1 MH/s (83.51ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 7700 - SAP CODVN B (BCODE)

Speed.#1.........:  4231.1 MH/s (78.54ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 7701 - SAP CODVN B (BCODE) mangled from RFC_READ_TABLE

Speed.#1.........:  4487.8 MH/s (74.03ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 7800 - SAP CODVN F/G (PASSCODE)

Speed.#1.........:  2434.3 MH/s (68.25ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 7801 - SAP CODVN F/G (PASSCODE) mangled from RFC_READ_TABLE

Speed.#1.........:  3715.4 MH/s (89.47ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 7900 - Drupal7 (Iterations: 16384)

Speed.#1.........:   128.3 kH/s (79.04ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 8000 - Sybase ASE

Speed.#1.........:   913.7 MH/s (91.10ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 8100 - Citrix NetScaler

Speed.#1.........: 14438.9 MH/s (92.09ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 8200 - 1Password, cloudkeychain (Iterations: 40000)

Speed.#1.........:    25509 H/s (80.83ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 8300 - DNSSEC (NSEC3)

Speed.#1.........:  6367.3 MH/s (52.16ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 8400 - WBB3 (Woltlab Burning Board)

Speed.#1.........:  2428.7 MH/s (68.39ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 8500 - RACF

Speed.#1.........:  6206.5 MH/s (53.51ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 8600 - Lotus Notes/Domino 5

Speed.#1.........:   706.1 MH/s (59.05ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 8700 - Lotus Notes/Domino 6

Speed.#1.........:   229.6 MH/s (90.86ms) @ Accel:64 Loops:16 Thr:256 Vec:1

Hashmode: 8800 - Android FDE <= 4.3 (Iterations: 2000)

Speed.#1.........:  1626.4 kH/s (48.83ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 8900 - scrypt (Iterations: 1)

Speed.#1.........:  1069.7 kH/s (14.74ms) @ Accel:16 Loops:1 Thr:16 Vec:1

Hashmode: 9000 - Password Safe v2 (Iterations: 1000)

Speed.#1.........:  1119.9 kH/s (46.27ms) @ Accel:512 Loops:250 Thr:8 Vec:1

Hashmode: 9100 - Lotus Notes/Domino 8 (Iterations: 5000)

Speed.#1.........:  1306.6 kH/s (49.00ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 9200 - Cisco-IOS $8$ (PBKDF2-SHA256) (Iterations: 20000)

Speed.#1.........:   144.8 kH/s (57.31ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 9300 - Cisco-IOS $9$ (scrypt) (Iterations: 1)

Speed.#1.........:    56137 H/s (128.21ms) @ Accel:16 Loops:1 Thr:8 Vec:1

Hashmode: 9400 - MS Office 2007 (Iterations: 50000)

Speed.#1.........:   266.9 kH/s (49.82ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 9500 - MS Office 2010 (Iterations: 100000)

Speed.#1.........:   133.4 kH/s (49.82ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 9600 - MS Office 2013 (Iterations: 100000)

Speed.#1.........:    21122 H/s (78.63ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 9700 - MS Office <= 2003 $0/$1, MD5 + RC4

Speed.#1.........:   837.3 MH/s (49.91ms) @ Accel:128 Loops:64 Thr:64 Vec:1

Hashmode: 9710 - MS Office <= 2003 $0/$1, MD5 + RC4, collider #1

Speed.#1.........:  1155.9 MH/s (68.02ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 9720 - MS Office <= 2003 $0/$1, MD5 + RC4, collider #2

Speed.#1.........:  4488.5 MH/s (74.16ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 9800 - MS Office <= 2003 $3/$4, SHA1 + RC4

Speed.#1.........:  1034.6 MH/s (80.71ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 9810 - MS Office <= 2003 $3, SHA1 + RC4, collider #1

Speed.#1.........:  1225.2 MH/s (63.88ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 9820 - MS Office <= 2003 $3, SHA1 + RC4, collider #2

Speed.#1.........:  6781.0 MH/s (49.06ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 9900 - Radmin2

Speed.#1.........: 19603.0 MH/s (67.79ms) @ Accel:128 Loops:512 Thr:256 Vec:4

Hashmode: 10000 - Django (PBKDF2-SHA256) (Iterations: 20000)

Speed.#1.........:   144.8 kH/s (57.32ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 10100 - SipHash

Speed.#1.........: 60665.4 MH/s (43.77ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 10200 - CRAM-MD5

Speed.#1.........:  8693.0 MH/s (76.46ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 10300 - SAP CODVN H (PWDSALTEDHASH) iSSHA-1 (Iterations: 1023)

Speed.#1.........: 10240.6 kH/s (44.22ms) @ Accel:128 Loops:255 Thr:256 Vec:1

Hashmode: 10400 - PDF 1.1 - 1.3 (Acrobat 2 - 4)

Speed.#1.........:  1287.6 MH/s (64.78ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 10410 - PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #1

Speed.#1.........:  1325.2 MH/s (58.72ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 10420 - PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2

Speed.#1.........: 16642.1 MH/s (79.87ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 10500 - PDF 1.4 - 1.6 (Acrobat 5 - 8) (Iterations: 70)

Speed.#1.........: 33560.8 kH/s (42.73ms) @ Accel:512 Loops:70 Thr:64 Vec:1

Hashmode: 10600 - PDF 1.7 Level 3 (Acrobat 9)

Speed.#1.........:  7624.8 MH/s (87.38ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 10700 - PDF 1.7 Level 8 (Acrobat 10 - 11) (Iterations: 64)

Speed.#1.........:    75352 H/s (135.71ms) @ Accel:16 Loops:2 Thr:256 Vec:1

Hashmode: 10800 - SHA2-384

Speed.#1.........:  2303.0 MH/s (72.13ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 10900 - PBKDF2-HMAC-SHA256 (Iterations: 999)

Speed.#1.........:  2801.0 kH/s (52.77ms) @ Accel:128 Loops:62 Thr:256 Vec:1

Hashmode: 11000 - PrestaShop

Speed.#1.........: 19346.0 MH/s (68.70ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 11100 - PostgreSQL CRAM (MD5)

Speed.#1.........: 15533.5 MH/s (85.58ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 11200 - MySQL CRAM (SHA1)

Speed.#1.........:  4361.6 MH/s (76.19ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 11300 - Bitcoin/Litecoin wallet.dat (Iterations: 199999)

Speed.#1.........:    10563 H/s (78.61ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 11400 - SIP digest authentication (MD5)

Speed.#1.........:  7499.0 MH/s (88.63ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 11500 - CRC32

Speed.#1.........: 13385.7 MH/s (49.62ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 11600 - 7-Zip (Iterations: 524288)

Speed.#1.........:    20557 H/s (61.52ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 11700 - GOST R 34.11-2012 (Streebog) 256-bit, big-endian

Speed.#1.........:   165.7 MH/s (63.05ms) @ Accel:32 Loops:16 Thr:256 Vec:1

Hashmode: 11750 - HMAC-Streebog-256 (key = $pass), big-endian

Speed.#1.........: 56339.5 kH/s (92.75ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 11760 - HMAC-Streebog-256 (key = $salt), big-endian

Speed.#1.........: 78100.5 kH/s (66.89ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 11800 - GOST R 34.11-2012 (Streebog) 512-bit, big-endian

Speed.#1.........:   165.7 MH/s (63.05ms) @ Accel:32 Loops:16 Thr:256 Vec:1

Hashmode: 11850 - HMAC-Streebog-512 (key = $pass), big-endian

Speed.#1.........: 48239.0 kH/s (54.18ms) @ Accel:16 Loops:8 Thr:256 Vec:1

Hashmode: 11860 - HMAC-Streebog-512 (key = $salt), big-endian

Speed.#1.........: 65230.3 kH/s (80.11ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 11900 - PBKDF2-HMAC-MD5 (Iterations: 999)

Speed.#1.........: 14564.9 kH/s (47.24ms) @ Accel:128 Loops:499 Thr:256 Vec:1

Hashmode: 12000 - PBKDF2-HMAC-SHA1 (Iterations: 999)

Speed.#1.........:  6024.8 kH/s (43.85ms) @ Accel:128 Loops:124 Thr:256 Vec:1

Hashmode: 12001 - Atlassian (PBKDF2-HMAC-SHA1) (Iterations: 9999)

Speed.#1.........:   661.3 kH/s (49.64ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 12100 - PBKDF2-HMAC-SHA512 (Iterations: 999)

Speed.#1.........:   933.6 kH/s (81.15ms) @ Accel:64 Loops:62 Thr:256 Vec:1

Hashmode: 12200 - eCryptfs (Iterations: 65535)

Speed.#1.........:    32240 H/s (78.62ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 12300 - Oracle T: Type (Oracle 12+) (Iterations: 4095)

Speed.#1.........:   248.8 kH/s (80.90ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 12400 - BSDi Crypt, Extended DES (Iterations: 2899)

Speed.#1.........:  4697.7 kH/s (85.10ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 12500 - RAR3-hp (Iterations: 262144)

Speed.#1.........:    82406 H/s (61.96ms) @ Accel:4 Loops:16384 Thr:256 Vec:1

Hashmode: 12600 - ColdFusion 10+

Speed.#1.........:  4139.1 MH/s (80.29ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 12700 - Blockchain, My Wallet (Iterations: 10)

Speed.#1.........: 52117.0 kH/s (7.91ms) @ Accel:128 Loops:10 Thr:256 Vec:1

Hashmode: 12800 - MS-AzureSync PBKDF2-HMAC-SHA256 (Iterations: 99)

Speed.#1.........: 20407.8 kH/s (88.39ms) @ Accel:128 Loops:99 Thr:256 Vec:1

Hashmode: 12900 - Android FDE (Samsung DEK) (Iterations: 4095)

Speed.#1.........:   705.9 kH/s (57.36ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 13000 - RAR5 (Iterations: 32767)

Speed.#1.........:    88397 H/s (57.34ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 13100 - Kerberos 5 TGS-REP etype 23

Speed.#1.........:   997.1 MH/s (83.67ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 13200 - AxCrypt (Iterations: 10000)

Speed.#1.........:   259.5 kH/s (64.05ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 13300 - AxCrypt in-memory SHA1

Speed.#1.........: 15464.9 MH/s (85.97ms) @ Accel:128 Loops:512 Thr:256 Vec:4

Hashmode: 13400 - KeePass 1 (AES/Twofish) and KeePass 2 (AES) (Iterations: 6000)

Speed.#1.........:   355.9 kH/s (77.82ms) @ Accel:512 Loops:128 Thr:32 Vec:1

Hashmode: 13500 - PeopleSoft PS_TOKEN

Speed.#1.........:  6185.1 MH/s (53.79ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 13600 - WinZip (Iterations: 1000)

Speed.#1.........:  2136.9 kH/s (69.39ms) @ Accel:128 Loops:62 Thr:256 Vec:1

Hashmode: 13711 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 512 bit (Iterations: 655331)

Speed.#1.........:     1893 H/s (66.30ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13712 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1024 bit (Iterations: 655331)

Speed.#1.........:     1060 H/s (59.64ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13713 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1536 bit (Iterations: 655331)

Speed.#1.........:      735 H/s (84.46ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 13721 - VeraCrypt PBKDF2-HMAC-SHA512 + XTS 512 bit (Iterations: 500000)

Speed.#1.........:     1877 H/s (88.13ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13722 - VeraCrypt PBKDF2-HMAC-SHA512 + XTS 1024 bit (Iterations: 500000)

Speed.#1.........:     1051 H/s (79.20ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13723 - VeraCrypt PBKDF2-HMAC-SHA512 + XTS 1536 bit (Iterations: 500000)

Speed.#1.........:      698 H/s (59.57ms) @ Accel:64 Loops:16 Thr:256 Vec:1

Hashmode: 13731 - VeraCrypt PBKDF2-HMAC-Whirlpool + XTS 512 bit (Iterations: 500000)

Speed.#1.........:      236 H/s (175.91ms) @ Accel:64 Loops:16 Thr:256 Vec:1

Hashmode: 13732 - VeraCrypt PBKDF2-HMAC-Whirlpool + XTS 1024 bit (Iterations: 500000)

Speed.#1.........:      118 H/s (176.96ms) @ Accel:32 Loops:16 Thr:256 Vec:1

Hashmode: 13733 - VeraCrypt PBKDF2-HMAC-Whirlpool + XTS 1536 bit (Iterations: 500000)

Speed.#1.........:       78 H/s (133.47ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 13741 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 512 bit + boot-mode (Iterations: 327661)

Speed.#1.........:     3784 H/s (66.35ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13742 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1024 bit + boot-mode (Iterations: 327661)

Speed.#1.........:     2119 H/s (59.66ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13743 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1536 bit + boot-mode (Iterations: 327661)

Speed.#1.........:     1471 H/s (84.42ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 13751 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 512 bit (Iterations: 500000)

Speed.#1.........:     2731 H/s (60.62ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13752 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 1024 bit (Iterations: 500000)

Speed.#1.........:     1356 H/s (61.27ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13753 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 1536 bit (Iterations: 500000)

Speed.#1.........:      896 H/s (91.59ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 13761 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 512 bit + boot-mode (Iterations: 200000)

Speed.#1.........:     6825 H/s (60.64ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13762 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 1024 bit + boot-mode (Iterations: 200000)

Speed.#1.........:     3389 H/s (61.27ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13763 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 1536 bit + boot-mode (Iterations: 200000)

Speed.#1.........:     2239 H/s (91.60ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 13771 - VeraCrypt PBKDF2-HMAC-Streebog-512 + XTS 512 bit (Iterations: 500000)

Speed.#1.........:      103 H/s (201.12ms) @ Accel:32 Loops:16 Thr:256 Vec:1

Hashmode: 13772 - VeraCrypt PBKDF2-HMAC-Streebog-512 + XTS 1024 bit (Iterations: 500000)

Speed.#1.........:       49 H/s (211.85ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 13773 - VeraCrypt PBKDF2-HMAC-Streebog-512 + XTS 1536 bit (Iterations: 500000)

Speed.#1.........:       33 H/s (159.83ms) @ Accel:16 Loops:8 Thr:256 Vec:1

Hashmode: 13800 - Windows Phone 8+ PIN/password

Speed.#1.........:  1871.5 MH/s (88.92ms) @ Accel:128 Loops:64 Thr:256 Vec:2

Hashmode: 13900 - OpenCart

Speed.#1.........:  4004.8 MH/s (82.94ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 14000 - DES (PT = $salt, key = $pass)

Speed.#1.........: 42848.1 MH/s (61.96ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 14100 - 3DES (PT = $salt, key = $pass)

Speed.#1.........:  2251.5 MH/s (74.33ms) @ Accel:8 Loops:1024 Thr:256 Vec:1

Hashmode: 14400 - sha1(CX)

Speed.#1.........:   728.9 MH/s (57.17ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 14600 - LUKS (Iterations: 163044)

Speed.#1.........:    19056 H/s (12.65ms) @ Accel:2 Loops:1024 Thr:256 Vec:1

Hashmode: 14700 - iTunes backup < 10.0 (Iterations: 9999)

Speed.#1.........:   331.6 kH/s (50.04ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 14800 - iTunes backup >= 10.0 (Iterations: 9999999)

Speed.#1.........:      288 H/s (3.53ms) @ Accel:2 Loops:250 Thr:256 Vec:1

Hashmode: 14900 - Skip32 (PT = $salt, key = $pass)

Speed.#1.........: 15639.4 MH/s (2.06ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 15000 - FileZilla Server >= 0.9.55

Speed.#1.........:  2467.4 MH/s (67.28ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 15100 - Juniper/NetBSD sha1crypt (Iterations: 19999)

Speed.#1.........:   335.1 kH/s (49.56ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 15200 - Blockchain, My Wallet, V2 (Iterations: 5000)

Speed.#1.........:   662.8 kH/s (49.46ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 15300 - DPAPI masterkey file v1 (Iterations: 23999)

Speed.#1.........:   137.9 kH/s (50.13ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 15400 - ChaCha20

Speed.#1.........:  8281.7 MH/s (80.20ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 15500 - JKS Java Key Store Private Keys (SHA1)

Speed.#1.........: 16220.3 MH/s (81.65ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 15600 - Ethereum Wallet, PBKDF2-HMAC-SHA256 (Iterations: 262143)

Speed.#1.........:    11040 H/s (57.34ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 15700 - Ethereum Wallet, SCRYPT (Iterations: 1)

Speed.#1.........:        6 H/s (8176.25ms) @ Accel:1 Loops:1 Thr:1 Vec:1

Hashmode: 15900 - DPAPI masterkey file v2 (Iterations: 7999)

Speed.#1.........:   119.2 kH/s (87.51ms) @ Accel:256 Loops:128 Thr:32 Vec:1

Hashmode: 16000 - Tripcode

Speed.#1.........:   570.5 MH/s (73.08ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 16100 - TACACS+

Speed.#1.........: 30629.1 MH/s (86.76ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 16200 - Apple Secure Notes (Iterations: 19999)

Speed.#1.........:   144.2 kH/s (57.53ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 16300 - Ethereum Pre-Sale Wallet, PBKDF2-HMAC-SHA256 (Iterations: 1999)

Speed.#1.........:  1416.7 kH/s (56.00ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 16400 - CRAM-MD5 Dovecot

Speed.#1.........: 54997.2 MH/s (48.25ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 16500 - JWT (JSON Web Token)

Speed.#1.........:  1286.6 MH/s (64.52ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 16600 - Electrum Wallet (Salt-Type 1-3)

Speed.#1.........:   563.2 MH/s (74.01ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 16700 - FileVault 2 (Iterations: 19999)

Speed.#1.........:   144.2 kH/s (57.53ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 16800 - WPA-PMKID-PBKDF2 (Iterations: 4096)

Speed.#1.........:   807.4 kH/s (49.99ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 16801 - WPA-PMKID-PMK (Iterations: 1)

Speed.#1.........: 54701.9 kH/s (0.02ms) @ Accel:128 Loops:1 Thr:256 Vec:1

Hashmode: 16900 - Ansible Vault (Iterations: 9999)

Speed.#1.........:   289.3 kH/s (57.37ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 17300 - SHA3-224

Speed.#1.........:  1716.4 MH/s (48.32ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17400 - SHA3-256

Speed.#1.........:  1711.6 MH/s (48.47ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17500 - SHA3-384

Speed.#1.........:  1711.8 MH/s (48.46ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17600 - SHA3-512

Speed.#1.........:  1712.0 MH/s (48.45ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17700 - Keccak-224

Speed.#1.........:  1716.5 MH/s (48.32ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17800 - Keccak-256

Speed.#1.........:  1711.5 MH/s (48.48ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17900 - Keccak-384

Speed.#1.........:  1711.5 MH/s (48.47ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 18000 - Keccak-512

Speed.#1.........:  1711.4 MH/s (48.46ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 18100 - TOTP (HMAC-SHA1)

Speed.#1.........:  2781.9 MH/s (59.67ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 18200 - Kerberos 5 AS-REP etype 23

Speed.#1.........:   989.8 MH/s (84.23ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 18300 - Apple File System (APFS) (Iterations: 19999)

Speed.#1.........:   144.3 kH/s (57.52ms) @ Accel:128 Loops:64 Thr:256 Vec:1
