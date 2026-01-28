if (
  ObjC.classes.PDDURLResponse &&
  ObjC.classes.PDDURLResponse['- setResponseData:']
) {
  Interceptor.attach(
    ObjC.classes.PDDURLResponse['- setResponseData:'].implementation,
    {
      onEnter(args) {
        try {
          const self = new ObjC.Object(args[0])
          const data = new ObjC.Object(args[2])

          console.log('\n========== 📥 setResponseData ==========')
          console.log('📦 Response:', self.toString())

          dumpNSData(data)

          console.log('========================================\n')
        } catch (e) {
          console.log('⚠️ Exception:', e)
        }
      },
    }
  )

  console.log('✅ Hooked PDDURLResponse -setResponseData:')
}

function dumpNSData(data) {
  if (!data || !data.isKindOfClass_(ObjC.classes.NSData)) {
    console.log('❌ Not NSData')
    return
  }

  const length = data.length()
  const bytes = data.bytes()

  console.log(`🧬 NSData length: ${length}`)

  if (length === 0) {
    console.log('⚠️ Empty NSData')
    return
  }

  console.log(
    hexdump(bytes, {
      length: Math.min(length, 512),
      header: true,
      ansi: false,
    })
  )

  // пробуем UTF‑8 (если это JSON / text)
  try {
    const str = Memory.readUtf8String(bytes, length)
    if (str && (str.includes('{') || str.includes('"'))) {
      console.log('📝 UTF‑8 preview:\n', str.slice(0, 500))
    }
  } catch (_) {}
}
