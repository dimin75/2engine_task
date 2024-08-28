curl -X PUT http://localhost:8000/api/tasks/{2}/ \
-H "Content-Type: application/json" \
-d '{"title": "Test_Task_Curl1", "description": "Updated description", "status": "in_progress"}'
