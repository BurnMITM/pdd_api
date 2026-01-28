var resolver = new ApiResolver('objc')

console.log('=== Безопасный мониторинг запущен ===')
console.log('Приложение PID: ' + Process.id)
console.log('Имя приложения: ' + Process.name)

// Используем более безопасный подход с try-catch
try {
  // Хукаем только ключевые методы
  resolver.enumerateMatches('-[* initWithURL*]', {
    onMatch: function (match) {
      try {
        // Пропускаем потенциально опасные методы
        if (match.name.includes('PDD') || match.name.includes('Private')) {
          console.log('[i] Пропускаем приватный метод: ' + match.name)
          return
        }

        Interceptor.attach(ptr(match.address), {
          onEnter: function (args) {
            try {
              // Безопасное получение URL
              var url = null
              var self = new ObjC.Object(args[0])

              // Для NSURLComponents
              if (
                match.name ===
                '-[NSURLComponents initWithURL:resolvingAgainstBaseURL:]'
              ) {
                var urlArg = new ObjC.Object(args[2]) // NSURL аргумент
                url = urlArg.absoluteString
                  ? urlArg.absoluteString().toString()
                  : urlArg.toString()
              }
              // Для NSURLRequest
              else if (match.name.includes('Request')) {
                var request = new ObjC.Object(args[2])
                url = request.URL()
                  ? request.URL().absoluteString().toString()
                  : 'Unknown URL'
              }
              // Для NSURL
              else if (match.name.includes('URL')) {
                url = new ObjC.Object(args[2]).toString()
              }

              if (url && url.includes('yangkeduo.com')) {
                console.log('\n=== НАЙДЕН ЗАПРОС ===')
                console.log('Метод: ' + match.name)
                console.log('URL: ' + url)
                console.log('Класс: ' + self.$className)

                // Безопасный бэктрейс (ограниченный)
                console.log('\nВызывающий стек (первые 10 фреймов):')
                try {
                  var backtrace = Thread.backtrace(
                    this.context,
                    Backtracer.ACCURATE
                  )
                  for (var i = 0; i < Math.min(backtrace.length, 10); i++) {
                    try {
                      var symbol = DebugSymbol.fromAddress(backtrace[i])
                      if (symbol) {
                        console.log('  [' + i + '] ' + symbol)
                      }
                    } catch (e) {}
                  }
                } catch (e) {
                  console.log('  Не удалось получить стек')
                }
              }
            } catch (e) {
              // Тихий fail
            }
          },

          onLeave: function (retval) {
            // Ничего не делаем в onLeave для безопасности
          },
        })

        console.log('[✓] Хук установлен: ' + match.name)
      } catch (e) {
        console.log('[✗] Ошибка хука ' + match.name + ': ' + e.message)
      }
    },
    onComplete: function () {
      console.log('[i] Поиск методов завершен')
    },
  })
} catch (e) {
  console.log('Критическая ошибка: ' + e.message)
}
