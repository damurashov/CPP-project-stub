set(EXECUTABLE @PROJECT_NAME@)
add_executable(@PROJECT_NAME@ "@PROJECT_NAME@/main.cpp")
target_link_libraries(@PROJECT_NAME@ @PROJECT_NAME@_3rd_party)
