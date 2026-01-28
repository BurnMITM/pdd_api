const base = Module.findBaseAddress('pinduoduo')

Interceptor.attach(base.add(0x1545bc), {
  onEnter(args) {
    this.input = args[0]
    this.inLen = args[1].toInt32()
    this.out = args[2]
    this.mode = args[3].toInt32()
    this.ctx = args[4]

    console.log('\n====== 🔐 sub_1001545BC ======')
    console.log('mode:', this.mode)

    if (this.inLen > 0 && this.inLen < 4096 && !this.input.isNull()) {
      try {
        // Пытаемся прочитать как UTF-8
        const s = Memory.readUtf8String(this.input, this.inLen)
        console.log('input (utf8):', s)
      } catch (e) {
        // Если это бинарь — спокойно делаем hexdump
        console.log('input (binary):')
        console.log(
          hexdump(Memory.readByteArray(this.input, this.inLen), {
            length: Math.min(this.inLen, 256),
          })
        )
      }
    } else {
      console.log('input len:', this.inLen)
    }

    console.log('ctx ptr:', this.ctx)
  },

  onLeave() {
    if (this.mode === 1) {
      const key = Memory.readByteArray(this.out, 32)
      console.log('🔥 DERIVED KEY:')
      console.log(hexdump(key, { length: 32 }))
    }

    if (this.mode === 2) {
      const sig = Memory.readByteArray(this.out, 32)
      console.log('✍️ SIGNATURE:')
      console.log(hexdump(sig, { length: 32 }))
    }

    console.log('====== END sub_1001545BC ======\n')
  },
})
