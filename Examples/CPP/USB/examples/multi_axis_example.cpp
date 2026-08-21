#include <xeryon.hpp>
#include <thread>
#include <chrono>
#include <iostream>
#include <vector>

using namespace xeryon;

static void wait_ms(int ms)
{
    auto end = std::chrono::steady_clock::now() + std::chrono::milliseconds(ms);

    while (std::chrono::steady_clock::now() < end)
    {
        std::this_thread::yield();
    }
}

int main()
{
    XController ctrl("COM4", 115200);

    if (!ctrl.connect())
    {
        std::cout << "Failed to connect XController\n";
        return -1;
    }

    Axis& axisA = ctrl.axis('A'); // MASTER
    Axis& axisB = ctrl.axis('B');
    Axis& axisC = ctrl.axis('C');

    std::vector<Axis*> axes = { &axisA, &axisB, &axisC };

    std::cout << "Waiting for all axes...\n";

    bool ready = false;
    while (!ready)
    {
        ready = true;

        for (auto ax : axes)
        {
            if (!ax->is_ready())
            {
                ready = false;
                break;
            }
        }

        wait_ms(2);
    }

    //Override if setting file path has changed
    //std::string configPath = R"(config\settings_default.txt)";

    axisA.applyDefaultSettings("");

    axisA.setUnit(Unit::MM);
    axisB.setUnit(Unit::MM);
    axisC.setUnit(Unit::MM);

    std::cout << "All axes ready (master A applied settings)\n";

    std::cout << "\n[1] INDEXING\n";

    for (auto ax : axes)
        ax->index(1);

    wait_ms(1500);

    std::cout << "\n[2] SCAN\n";

    for (auto ax : axes)
        ax->setScan(-1);

    wait_ms(2000);

    for (auto ax : axes)
        ax->setScan(1);

    wait_ms(2000);

    for (auto ax : axes)
        ax->setScan(0);

    wait_ms(1000);

    for (auto ax : axes)
        ax->setSpeed(10);

    std::cout << "\n[3] POSITION SWEEP\n";

    for (auto ax : axes)
        ax->index(1);

    wait_ms(1500);

    axisA.setDPOS(25);
    axisB.setDPOS(10);
    axisC.setDPOS(-5);

    wait_ms(1000);

    axisA.setDPOS(-25);
    axisB.setDPOS(-10);
    axisC.setDPOS(5);

    wait_ms(1000);

    std::cout << "\n[4] STEP LOOP\n";
    for (auto ax : axes)
        ax->index(1);

    wait_ms(1500);

    for (int i = 0; i < 12; ++i)
    {
        for (auto ax : axes)
            ax->setStep(1);

        wait_ms(500);
    }

    for (int i = 0; i < 24; ++i)
    {
        for (auto ax : axes)
            ax->setStep(-1);

        wait_ms(500);
    }

    std::cout << "\n[5] HOME ALL\n";
    for (auto ax : axes)
        ax->home();

    wait_ms(1500);

    std::cout << "\nDone. Disconnecting...\n";
    ctrl.disconnect();

    return 0;
}
