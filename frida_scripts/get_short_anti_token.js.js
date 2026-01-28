console.log('✅ Frida short anti token hook loaded')

const TMRiskManagement = ObjC.classes.TMRiskManagement

Interceptor.attach(TMRiskManagement['- parametersWithParams:'].implementation, {
  onEnter(args) {
    console.log('\n========== [parametersWithParams:] ==========')

    const self = new ObjC.Object(args[0])
    const params = new ObjC.Object(args[2])

    console.log('📦 Params NSDictionary:')

    try {
      const enumerator = params.keyEnumerator()
      let key
      while ((key = enumerator.nextObject()) !== null) {
        const value = params.objectForKey_(key)
        console.log(`  ${key.toString()} = ${value.toString()}`)
      }
    } catch (e) {
      console.log('⚠️ Failed to enumerate params:', e)
    }
  },

  onLeave(retval) {
    if (retval.isNull()) {
      console.log('❌ Returned NULL')
      return
    }

    const data = new ObjC.Object(retval)
    const length = data.length()
    const bytes = data.bytes()

    console.log('🧬 Risk NSData length:', length)

    const raw = Memory.readByteArray(bytes, length)
    console.log(
      '🧬 Risk NSData HEX:\n' +
        hexdump(raw, {
          offset: 0,
          length: length,
          header: false,
          ansi: false,
        })
    )

    console.log('============================================\n')
  },
})
