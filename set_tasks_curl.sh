curl -X POST http://localhost:8000/api/tasks/ -H "Content-Type: application/json" -d '{"title": "Test_Task_Curl1", "description": "Task from Curl 1", "status": "queued"}'
curl -X POST http://localhost:8000/api/tasks/ -H "Content-Type: application/json" -d '{"title": "Test_Task_Curl2", "description": "Task from curl 2", "status": "queued"}'
