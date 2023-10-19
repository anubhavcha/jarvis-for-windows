import speedtest


def test_speed():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    ping = st.results.ping

    print(f"Download Speed: {download_speed / 1_000_000:.2f} Mbps")
    print(f"Upload Speed: {upload_speed / 1_000_000:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")



