# 🎮 Lsfg-Gui

**Lsfg-Gui** is a user-friendly tool to configure and launch [`lsfg-vk`](https://github.com/PancakeTAS/lsfg-vk) with ease on Linux systems. It provides a simple graphical interface to limit FPS in Vulkan games and applications.

---

## 🚀 Usage

```bash
python3 main.py
```

### 🖥️ How it works

1. Launch **Lsfg-Gui**.
2. Select the target process (game) from the list.
3. Set your desired FPS limit.
4. Click **Apply** — the limiter will attach to the selected Vulkan process.

---

## 📋 Features & Recommendations

* 🖱️ Clean graphical interface — no terminal needed.
* 🎯 Automatically detects running Vulkan applications.
* ⚙️ Configures and launches `lsfg-vk` with correct parameters.
* 💡 Ideal for reducing input lag or saving power on limited devices.

---

## 🔧 Dependencies

* `lsfg-vk` (must be built separately from [PancakeTAS/lsfg-vk](https://github.com/PancakeTAS/lsfg-vk))
* Vulkan-compatible GPU and driver
* PyQt5

---

## 🧩 Notes

* 🔄 Restart the game if the limiter does not apply immediately.
* 🧪 Not all Vulkan games may behave the same — test for stability.
* 🐧 Works well with native Vulkan programs.
