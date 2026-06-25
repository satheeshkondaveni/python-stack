A sudden shutdown on your HP Pavilion laptop—even when the battery shows 81%—usually points to hardware or system issues beyond just battery charge. Here’s how you can systematically check it:

### 🔍 Step-by-Step Checks
1. **Overheating**
   - Laptops shut down automatically if the CPU/GPU overheats.
   - Check if the fan is running loudly or if the laptop feels unusually hot.
   - Use **HP Hardware Diagnostics (F2 at startup)** or install a tool like *HWMonitor* to check temperatures.

2. **Battery & Power Supply**
   - Even if it shows 81%, the battery may be faulty.
   - Try running the laptop only on AC power (remove the battery if possible).
   - In Windows, run:  
     - **Win + X → Windows PowerShell → `powercfg /batteryreport`**  
     - This generates a battery health report.

3. **Event Viewer Logs**
   - Press **Win + R → type `eventvwr.msc` → Enter**.
   - Navigate to **Windows Logs → System**.
   - Look for **Critical errors** around the time of shutdown (often “Kernel-Power” events).

4. **Driver & BIOS Updates**
   - Outdated BIOS or drivers can cause instability.
   - Go to HP Support → enter your laptop model → update BIOS, chipset, and graphics drivers.

5. **Hardware Diagnostics**
   - Restart and press **F2** → run HP’s built-in diagnostics.
   - This will test memory, hard drive, and battery.

6. **Malware or Corrupted System Files**
   - Run **Windows Security Scan**.
   - Open Command Prompt (Admin) → run:  
     - `sfc /scannow` (checks system files)  
     - `chkdsk /f` (checks disk errors)

---

⚠️ **Quick tip:** If the shutdown happens only when plugged in, it could be a faulty charger or power circuit. If it happens randomly, overheating or hardware faults are more likely.

👉 Do you want me to guide you through generating the **battery health report** first, or checking the **Event Viewer logs**? Those two will quickly tell us if it’s a battery issue or a system crash.