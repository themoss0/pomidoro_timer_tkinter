from enum import Enum

class State(Enum):
    IDLE: str = 'IDLE'
    PAUSED: str = 'PAUSED'
    WORK: str = 'WORK'
    REST: str = 'REST'
    LONG_REST: str = 'LONG_REST'

class Time(Enum):
    '''Пресеты времени: мм:сс/мм:сс/мм:сс'''
    TIME_DEBUG: str = '00:15/00:20/30:00'

    TIME_25_05_30: str = '25:00/05:00/30:00'
    TIME_15_03_20: str = '15:00/03:00/20:00'
    TIME_30_05_30: str = '30:00/05:00/30:00'
    TIME_30_10_25: str = '30:00/10:00/25:00'
    TIME_45_10_30: str = '45:00/10:00/30:00'
    TIME_50_15_30: str = '50:00/15:00/30:00'
    TIME_60_10_60: str = '60:00/10:00/60:00'
    TIME_180_30_60: str = '180:00/30:00/60:00'



class TimerViewModel:
    def __init__(self, default_state: State, time_interval: Time):
        self.running: bool = False
        self.is_rest: bool = False
        self.state: State = default_state
        self.time: Time = time_interval
        self.cycle_count: int = 0

    def get_seconds_of_time(self) -> list:
        # Возвращает список секунд, где: 
        # seconds[0] - Секунды работы
        # seconds[1] - Секунды обычного перерыва
        # seconds[2] - Секунды длительного перерыва

        seconds: list = [0, 0, 0]
        time_strings: list = self.time.value.split('/')
        time_separated: list = []
        for i in range(len(time_strings)):
            time_separated.append(time_strings[i].split(':'))
        
        for i in range(len(time_separated)):
            result_time_sec = int(time_separated[i][0]) * 60 + int(time_separated[i][1])
            seconds[i] = result_time_sec
        # print(time_strings)
        # print(time_separated)
        # print(seconds)

        return seconds

    def set_time_preset(self, new_preset: Time):
        self.time = new_preset
    
    def set_rest_configuration(self):
        self.running = True
        self.is_rest = True
        self.state = State.REST

    
    def set_long_rest_configuration(self):
        self.running = True
        self.is_rest = True
        self.state = State.LONG_REST
        self.cycle_count = 0
        
    
    def set_work_configuration(self):
        self.running = True
        self.is_rest = False
        self.state = State.WORK
        

    def set_paused_configuration(self):
        self.running = False
        self.state =State.PAUSED


    def set_reset_configuration(self):
        self.running = False
        self.is_rest = False
        self.state = State.IDLE
        self.cycle_count = 0

    def set_running_mode(self, mode: bool) -> None:
        # print(f"DEBUG: TimeViewModel.set_running_mode() worked:" )
        # print('--------------------------------')
        # print(f"Recent running mode: {self.running}")
        
        self.running = mode

        # print(f"Current running mode: {self.running}")
        # print('--------------------------------')
        # print()

    def set_is_rest_mode(self, mode: bool) -> None:
        # print(f"DEBUG: TimeViewModel.set_is_rest_mode() worked:" )
        # print('--------------------------------')
        # print(f"Recent is_rest mode: {self.is_rest}")

        self.is_rest = mode

        # print(f"Current is_rest mode: {self.is_rest}")
        # print('--------------------------------')


    def set_state(self, new_state: State) -> None:
        # print(f"DEBUG: TimeViewModel.set_state() worked:" )
        # print('--------------------------------')
        # print(f"Recent state: {self.state}")
        self.state = new_state
        # print(f"Current state: {self.state}")
        # print('--------------------------------')
        # print()

    def get_state(self) -> State:
        # print(f"DEBUG: TimeViewModel.get_state() worked:" )
        # print('--------------------------------')
        # print(f"Current state: {self.state}")
        # print('--------------------------------')
        # print()
        return self.state
    
    def get_running_mode(self) -> bool:
        # print(f"DEBUG: TimeViewModel.get_running_mode() worked:" )
        # print('--------------------------------')
        # print(f"Current state: {self.running}")
        # print('--------------------------------')
        # print()
        
        return self.running

    def change_running_mode(self) -> None:
        # print(f"DEBUG: TimeViewModel.change_running_mode() worked:" )
        # print('--------------------------------')
        # print(f"Recent state: {self.state}")

        self.running = not self.running

        # print(f"Current state: {self.state}")
        # print('--------------------------------')
        # print()

    def display(self) -> None:
        print(f"DEBUG: TimeViewModel.display() worked:" )
        print('--------------------------------')
        print(f"Current running mode: {self.running}")
        print(f"Current is_rest mode: {self.is_rest}")
        print(f"Current state: {self.state}")
        print('--------------------------------')
        print()

