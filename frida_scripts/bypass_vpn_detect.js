if (ObjC.available) {
  var cls = ObjC.classes.AMPMMStatus
  var sel = '- isNetworkVPN'

  Interceptor.attach(cls[sel].implementation, {
    onEnter(args) {
      this.self = new ObjC.Object(args[0])
      console.log('📡 AMPMMStatus isNetworkVPN called')
      console.log('self:', this.self)
    },
    onLeave(retval) {
      retval.replace(0x0)
    },
  })
}
