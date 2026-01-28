function dumpNSDictionary(dict) {
  const result = {}

  const enumerator = dict.keyEnumerator()
  let key

  while ((key = enumerator.nextObject()) !== null) {
    const value = dict.objectForKey_(key)
    result[key.toString()] = value ? value.toString() : null
  }

  return result
}

const PDDURLRequest = ObjC.classes.PDDURLRequest

Interceptor.attach(PDDURLRequest['- setHeaders:'].implementation, {
  onEnter(args) {
    const headers = new ObjC.Object(args[2])

    console.log('\n=== setHeaders ===')
    console.log(JSON.stringify(dumpNSDictionary(headers), null, 2))
  },
})

Interceptor.attach(PDDURLRequest['- setFullURL:'].implementation, {
  onEnter(args) {
    console.log('=== FULL URL ===', new ObjC.Object(args[2]).toString())
  },
})

// Interceptor.attach(PDDURLRequest['- bodyData'].implementation, {
//   onLeave(retval) {
//     if (!retval.isNull()) {
//       const data = new ObjC.Object(retval)
//       const len = data.length()
//       const bytes = data.bytes()
//       console.log('=== BODY ===')
//       console.log(Memory.readUtf8String(bytes, len))
//     }
//   },
// })
