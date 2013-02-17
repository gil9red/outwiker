��          �   %   �      0  $   1  *   V  &   �  [  �  
                   .     3     9     G     Y     g     o     �  
   �     �     �     �     �     �     �  )     �  /  ;   �  <    	  E   ]	  �  �	     �  *   �  #   �            <     7   [     �  
   �  >   �     �       ,        G     e  
   �  N   �  #   �  '        
                                      	                                                                                    <B>Source plugin: Encoding error</B> <B>Source plugin: File '{0}' not found</B> <B>Source plugin: Unknown encoding</B> Add command (:source:) in wiki parser. This command highlight your source code.

<B>Usage:</B>:
(:source params... :)
source code
(:sourceend:)

<B>Params:</B>
<I>lang</I> - programming language
<I>tabwidth</I> - tab size
<I>file</I> - attached source file
<I>encoding</I> - encoding of the attached source file (default encoding - utf8)
<I>style</I> - style of hightlighting

<B>Example 1:</B>
<PRE>(:source lang="python" tabwidth=4:)
import os

if __name__ == "__main__":
    print "Hello World!"
(:sourceend:)
</PRE>

<B>Example 2:</B>
<PRE>(:source lang="python" style="autumn":)
import os

if __name__ == "__main__":
    print "Hello World!"
(:sourceend:)
</PRE>

<B>Example 3:</B>
<PRE>(:source file="Attach:example.cs" encoding="cp1251":)(:sourceend:)</PRE>

<B>Example 4:</B>
<PRE>(:source file="Attach:example.txt" lang="python":)(:sourceend:)</PRE>
 Appearance Attach new files Attached file Auto Clear Default Style Default Tab Width File encoding General Insert source from file Language Select All Source Code (:source ...:) Source [Plugin] Source code Style Tab Width (0 - Default Value) Used Languages http://jenyay.net/Outwiker/SourcePluginEn Project-Id-Version: SourcePlugin 1.0
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2013-02-17 14:10+0400
PO-Revision-Date: 2013-02-17 14:11+0300
Last-Translator: Eugeniy Ilin <jenyay.ilin@gmail.com>
Language-Team: Jenyay <jenyay.ilin@gmail.com>
Language: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Poedit-Language: Russian
X-Poedit-Country: RUSSIAN FEDERATION
X-Poedit-SourceCharset: utf-8
 <B>Плагин Source: Ошибка кодировки</B> <B>Плагин Source: Файл '{0}' не найден</B> <B>Плагин Source: Неизвестная кодировка</B> Расширение добавляет вики-команду (:source:) для раскраски текста программы на различных языках программирования.

<B>Использование:</B>:
(:source параметры... :)
Исходный код
(:sourceend:)

<B>Параметры:</B>
<I>lang</I> - язык программирования
<I>tabwidth</I> - размер табуляции
<I>file</I> - прикрепленный файл с текстом программы
<I>encoding</I> - кодировка прикрепленного файла с текстом программы (кодировка по умолчанию - utf8)
<I>style</I> - используемый стиль оформления

<B>Пример 1:</B>
<PRE>(:source lang="python" tabwidth=4:)
import os

if __name__ == "__main__":
    print "Hello World!"
(:sourceend:)
</PRE>

<B>Пример 2:</B>
<PRE>(:source lang="python" style="autumn":)
import os

if __name__ == "__main__":
    print "Hello World!"
(:sourceend:)
</PRE>

<B>Пример 3:</B>
<PRE>(:source file="Attach:example.cs" encoding="cp1251":)(:sourceend:)</PRE>

<B>Пример 4:</B>
<PRE>(:source file="Attach:example.txt" lang="python":)(:sourceend:)</PRE>
 Внешний вид Прикрепить новые файлы Прикрепленный файл Авто Очистить Стиль, используемый по умолчанию Размер табуляции по умолчанию Кодировка файла Общее Вставить текст программы из файла Язык Выбрать все Текст программы (:source ...:) Source [Расширение] Текст программы Стиль Размер табуляции (0 - значение по умолчанию) Используемые языки http://jenyay.net/Outwiker/SourcePlugin 