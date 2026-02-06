
if (ObjC.available) {
  const cls = ObjC.classes.HeraWWANIpv6Util
  const method = cls['+ getWWANIpv6:']

  Interceptor.attach(method.implementation, {
    onEnter(args) {
      this.statusPtr = args[2]
    },
    onLeave(retval) {
      let status = -1
      if (!this.statusPtr.isNull()) {
        status = Memory.readU64(this.statusPtr)
      }

      console.log('[getWWANIpv6] status =', status)

      if (!retval.isNull()) {
        const dict = new ObjC.Object(retval)
        console.log('[getWWANIpv6] return =', dict.toString())
      } else {
        console.log('[getWWANIpv6] return = nil')
      }
    },
  })

  console.log('[+] Hooked +[HeraWWANIpv6Util getWWANIpv6:]')
}
