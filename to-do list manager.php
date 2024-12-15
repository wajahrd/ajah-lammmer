<?php

// 2. To-Do List Manager (PHP)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    session_start();

    // Initialize tasks if not already
    if (!isset($_SESSION['tasks'])) {
        $_SESSION['tasks'] = [];
    }

    $action = $_POST['action'] ?? '';

    if ($action === 'add') {
        $task = $_POST['task'] ?? '';
        if (!empty($task)) {
            $_SESSION['tasks'][] = $task;
        }
    } elseif ($action === 'remove') {
        $taskIndex = $_POST['task_index'] ?? -1;
        if (isset($_SESSION['tasks'][$taskIndex])) {
            unset($_SESSION['tasks'][$taskIndex]);
            $_SESSION['tasks'] = array_values($_SESSION['tasks']); // Re-index array
        }
    }
}

?>