#include <string>
#include <vector>

struct Todo {
    int id;
    std::string title;
    std::string date;
    std::string content;
    bool done;
};

class Todomanager {
public:
    Todomanager();
    ~Todomanager();
    void addTodo(std::string title, std::string date, std::string content);
    void deleteTodo();
    void loadfile();
    void updatefile();
private:
    std::vector<Todo> Todosave;
    int now_id;
};
