# Meta Info Request Encryption (iOS Reverse Engineering Notes)

This repository documents the encryption flow and runtime analysis of a request sent to the endpoint:

POST /project/meta_info HTTP/2


The request body has the following structure:

```json
{
  "key": "%s",
  "data": "%s"
}
```

## 🔐 Encryption Scheme

The encryption logic works as follows:

```
key  = RSA(public_key, key_AES)
data = AES_256_CBC(body, key_AES)
```

```
key_AES — randomly generated AES key
key — AES key encrypted using RSA (public key required)
data — request body encrypted with AES-256-CBC

Current Problems
Extracting the RSA public key
Understanding what exact data is placed into the encrypted body
```

## 🧠 Runtime Analysis (LLDB)

List all methods of TMNGPDFP

```
po [[objc_getClass("TMNGPDFP") alloc] _methodDescription]

po [[objc_getClass("TMNGPDFP") alloc] _methodDescription]
<TMNGPDFP: 0x28302c570>:
in TMNGPDFP:
	Class Methods:
		+ (id) allocWithZone:(struct _NSZone*)arg1; (0x101265298)
		+ (id) sharedInstance; (0x101265290)
	Instance Methods:
		- (void) parseExtra:(id)arg1 append:(id)arg2 forKey:(id)arg3 putKey:(id)arg4; (0x101265358)
		- (id) encodeBase64:(id)arg1; (0x101265350)
		- (id) decodeBase64:(id)arg1; (0x101265348)
		- (long) getFunctionAddr:(id)arg1; (0x101265340)
		- (id) getEntitlements2; (0x101265338)
		- (id) getEntitlements; (0x101265330)
		- (id) getMemoryInject2; (0x101265328)
		- (id) getMemoryInject; (0x101265320)
		- (id) getBacktrace; (0x101265318)
		- (id) getGestaltPlistResult; (0x101265310)
		- (BOOL) stableWithGrayID:(long)arg1; (0x101265308)
		- (BOOL) enableWithGrayID:(long)arg1; (0x101265300)
		- (id) getExtraInfo; (0x1012652f8)
		- (id) sdkVersion; (0x1012652f0)
		- (id) PDFPExtraInfo; (0x1012652e8)
		- (id) signInfo; (0x1012652e0)
		- (BOOL) RS; (0x1012652d8)
		- (id) PDFPWithParams:(id)arg1 extra:(id)arg2; (0x1012652d0)
		- (id) PDFPWithParams:(id)arg1; (0x1012652c8)
		- (id) mutableCopyWithZone:(struct _NSZone*)arg1; (0x1012652c0)
		- (id) copyWithZone:(struct _NSZone*)arg1; (0x1012652b8)
```

Generate Encrypted Payload

```
(lldb) e id $dict = [NSMutableDictionary dictionary]
(lldb) e (void)[$dict setObject:@"1" forKey:@"scene"]
(lldb) e (void)[$dict setObject:@"test" forKey:@"pddid"]
(lldb) e (void)[$dict setObject:@"192.168.1.1" forKey:@"ip"]
(lldb) e id $tmngpdfp = (id)[objc_getClass("TMNGPDFP") sharedInstance]
(lldb) e id $result = (id)[$tmngpdfp PDFPWithParams:$dict]

po $$result
➡️ $result returns the final structure:
{
  "key": "%s",
  "data": "%s"
}
```

## 🧩 VM-Based Logic

- The class TMNGPDFP is generated through a virtual machine (VM)
- Core logic is evaluated inside:

```
bool __cdecl -[Proxima evalData:](Proxima *self, SEL a2, id a3)
```

## 🤝 Help Wanted

- If you have experience reversing:
- Custom VMs
- iOS crypto pipelines
- Runtime deobfuscation

Telegram: diduk12