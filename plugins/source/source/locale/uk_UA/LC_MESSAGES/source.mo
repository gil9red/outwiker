��          �      L      �  $   �  *   �  &     �  8     �     �     �     �               +  
   4     ?     Z     j     v     �  )   �  �  �  ?   z  B   �  A   �  �  ?     >     Z     c  ?   t     �  :   �            *   .     Y     q  V   �  /   �  '                          
                       	                                                      <B>Source plugin: Encoding error</B> <B>Source plugin: File '{0}' not found</B> <B>Source plugin: Unknown encoding</B> Add command (:source:) in wiki parser. This command highlight your source code.

<B>Usage:</B>:
(:source params... :)
source code
(:sourceend:)

<B>Params:</B>
<I>lang</I> - programming language
<I>tabwidth</I> - tab size
<I>file</I> - attached source file
<I>encoding</I> - encoding of the attached source file (default encoding - utf8)

<B>Example 1:</B>
<PRE>(:source lang="python" tabwidth=4:)
import os

if __name__ == "__main__":
    print "Hello World!"
(:sourceend:)
</PRE>

<B>Example 2:</B>
<PRE>(:source file="Attach:example.cs" encoding="cp1251":)(:sourceend:)</PRE>

<B>Example 3:</B>
<PRE>(:source file="Attach:example.txt" lang="python":)(:sourceend:)</PRE>
 Attached file Auto Clear Default Tab Width File encoding Insert source from file Language Select All Source Code (:source ...:) Source [Plugin] Source code Tab Width (0 - Default Value) Used Languages http://jenyay.net/Outwiker/SourcePluginEn Project-Id-Version: outwiker
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2013-01-19 10:06+0400
PO-Revision-Date: 2013-01-19 17:52+0300
Last-Translator: Eugeniy Ilin <jenyay.ilin@gmail.com>
Language-Team: Ukrainian
Language: uk_UA
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Generator: crowdin.net
X-Poedit-Language: Ukrainian
X-Poedit-Country: UKRAINE
X-Poedit-SourceCharset: utf-8
 <B>Додаток Source: Помилка кодування</B> <B>Додаток Source: Файл '{0}' не знайдено</B> <B>Додаток Source: Невідоме кодування</B> Додаток додає вікі-команду (:source:) для розфарбовування тексту програми на різних мовах програмування.

<B>Використання:</B>:
(:source параметри... :)
Програмний код
(:sourceend:)

<B>Параметри:</B>
<I>lang</I> - мова програмування
<I>tabwidth</I> - розмір табуляції
<I>file</I> - долучений файл з текстом програми
<I>encoding</I> - кодування долученого файлу з текстом програми (кодування за замовчуванням - utf8)

<B>Приклад 1:</B>
<PRE>(:source lang="python" tabwidth=4:)
import os

if __name__ == "__main__":
    print "Hello World!"
(:sourceend:)
</PRE>

<B>Приклад 2:</B>
<PRE>(:source file="Attach:example.cs" encoding="cp1251":)(:sourceend:)</PRE>

<B>Приклад 3:</B>
<PRE>(:source file="Attach:example.txt" lang="python":)(:sourceend:)</PRE>
 Долучений файл Авто Очистити Ширина табуляції за замовчуванням Кодування файлу Вставити текст програми з файлу Мова Виділити все Текст програми (:source ...:) Source [Додаток] Текст програми Ширина табуляції (0 - значення за замовчуванням) Мови, що використовуються http://jenyay.net/Outwiker/SourcePlugin 