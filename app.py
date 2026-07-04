import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# In-memory база данных для наших задач
TASKS = ["Buy milk", "Learn Python"]

class TodoRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Возвращаем главную страницу (HTML)
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            
            # Генерируем HTML-список задач
            tasks_li = "".join([f"<li>{task}</li>" for task in TASKS])
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Todo App</title>
                <style>
                    body {{ font-family: sans-serif; padding: 40px; background: #f0f2f5; }}
                    .container {{ max-width: 500px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
                    h1 {{ color: #333; }}
                    ul {{ list-style-type: square; padding-left: 20px; }}
                    li {{ padding: 8px 0; font-size: 18px; color: #555; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>My Tasks</h1>
                    <ul id="task-list">
                        {tasks_li}
                    </ul>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
            
        # 2. API endpoint для получения списка задач в формате JSON
        elif self.path == "/api/tasks":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {"tasks": TASKS}
            self.wfile.write(json.dumps(response).encode("utf-8"))
            
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        # 3. API endpoint для добавления новой задачи
        if self.path == "/api/tasks":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode("utf-8"))
                new_task = data.get("task")
                
                if new_task:
                    TASKS.append(new_task)
                    self.send_response(201)  # Created
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    response = {"status": "success", "task": new_task}
                    self.wfile.write(json.dumps(response).encode("utf-8"))
                else:
                    self.send_response(400)
                    self.end_headers()
            except Exception as e:
                self.send_response(500)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def run_server(port=5000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, TodoRequestHandler)
    print(f"Starting local server on http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
