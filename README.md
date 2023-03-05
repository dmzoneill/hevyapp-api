# hevy-api

![Bench press](https://github.com/dmzoneill/hevyapp-api/blob/main/img/sample.png?raw=true)

## Samples

- [Samples](https://github.com/dmzoneill/hevyapp-api/tree/main/sample)
- [Python pyplot example](https://dmzoneill.github.io/hevyapp-api/sample/chart.html)
- [Chart js example](https://dmzoneill.github.io/hevyapp-api/sample/5.chart.html)

## Overviews

- [login.md](https://github.com/dmzoneill/hevyapp-api/blob/main/api/login.md)
- [account.md](https://github.com/dmzoneill/hevyapp-api/blob/main/api/account.md)
- [workoutcount.md](https://github.com/dmzoneill/hevyapp-api/blob/main/api/workoutcount.md)
- [feed_workouts_paged.md](https://github.com/dmzoneill/hevyapp-api/blob/main/api/feed_workouts_paged.md)
- [routines_sync_batched.md](https://github.com/dmzoneill/hevyapp-api/blob/main/api/routines_sync_batched.md)
- [user_preferences.md](https://github.com/dmzoneill/hevyapp-api/blob/main/api/user_preferences.md)


## How to dissect https calls for yourself

### Download

 - Android studio
 - [Charles proxy](https://www.charlesproxy.com/)
 - [apk-mitm](https://www.npmjs.com/package/apk-mitm/)
 - [com.hevy apk](https://m.apkpure.com/hevy-gym-log-workout-tracker/com.hevy/download)

### Setup

1. Open android studio
2. Create an android virtual device
3. Boot the device
4. Download the hevy app apk
5. Download apk-mitm
6. Patch the apk as described on [apk-mitm](https://www.npmjs.com/package/apk-mitm/)
7. Install charles proxy
8. Install the certificate and setup the proxy on the android device as described here:
 https://blog.logrocket.com/test-debug-android-apps-with-charles-web-proxy/
9. Using android studio upload the patched APK to the android device and then install it
10. open hevy app and login

Hevy should use the proxy with the previously installed certificate and in charles you can now see the decrypted https requests.