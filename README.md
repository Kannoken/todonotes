## Добавление новой записки/напоминания 
<pre>
curl -X POST -H 'Content-Type:application/json' -d '{"description":"You added me!"}' http://localhost:8000/todos/
</pre>
## Запрос всех созданных напоминаний 
<pre>
curl -X POST -H 'Content-Type:application/json'
</pre>
## Удаление записи (добавление id в ссылке)
<pre>
 curl -X DELETE -H 'Content-Type:application/json' -d '{"description":"test11"}' http://localhost:8000/todos/1 
</pre>

## Изменение записи (добавление id в ссылке)
<pre>
 curl -X PUT -H 'Content-Type:application/json' -d '{"description":"test12", "is_done":"True"}' http://localhost:8000/todos/2
</pre>
