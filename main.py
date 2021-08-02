import socket
import struct

'''
StateData is a class representing the state of the robot.
The data is sent from the robot to the program.
'''
class StateData:
    def __init__(self) -> None:
        pass

    def __init__(self, data_tuple) -> None:
        (
            self.left_motor_speed,
            self.right_motor_speed,
            self.water_leakage_data,
            self.camera_pitch_angle,
            self.compass,
            self.rake_angle,
            self.pitch_angle,
            self.sidewides_flag,
            self.roll_data,
            self.depth,
            self.clear_flag,
            self.water_temperature,
            self.sonar_pitch_angle,
            self.cumulative_checksum,
        ) = data_tuple
        pass

    @staticmethod
    def parse_raw_bytes(raw_bytes):
        src = struct.unpack(">xxxxHHccHcHcHicHcH", raw_bytes)
        return src

    def __str__(self) -> str:
        return f"{self.left_motor_speed}, {self.right_motor_speed}"


'''
Construct control data to be sent to the robot.
'''
def control(
    action,
    speed_left,
    speed_right,
    camera_action,
    camera_speed,
    sonar_action,
    sonar_speed,
    light_switch,
    depth_reset,
    light_tune,
):
    light_switch_depth_reset = light_switch | (depth_reset << 1)
    payload = b"\xFF\xFE\xFF\xFE" + struct.pack(
        ">bBBBBBBBB",
        action,
        speed_left,
        speed_right,
        camera_action,
        camera_speed,
        sonar_action,
        sonar_speed,
        light_switch_depth_reset,
        light_tune,
    )
    checksum = sum(list(payload))
    payload += struct.pack(">H", checksum)
    return payload



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.235", 20108))

    while True:
        recv_data = s.recv(28)
        print(recv_data)
        state = StateData(StateData.parse_raw_bytes(recv_data))
        print(state)
        s.send(control(1, 2, 3, 0, 7, 0, 7, 1, 0, 0))

if __name__ == "__main__":
    main()
