// Copyright 2020 Northern.tech AS
//
//    Licensed under the Apache License, Version 2.0 (the "License");
//    you may not use this file except in compliance with the License.
//    You may obtain a copy of the License at
//
//        http://www.apache.org/licenses/LICENSE-2.0
//
//    Unless required by applicable law or agreed to in writing, software
//    distributed under the License is distributed on an "AS IS" BASIS,
//    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//    See the License for the specific language governing permissions and
//    limitations under the License.

package config

import (
	"github.com/mendersoftware/go-lib-micro/config"
)

const (
	// SettingListen is the config key for the listen address
	SettingListen = "listen"
	// SettingListenDefault is the default value for the listen address
	SettingListenDefault = ":8080"

	// SettingNatsURI is the config key for the nats uri
	SettingNatsURI = "nats_uri"
	// SettingNatsURIDefault is the default value for the nats uri
	SettingNatsURIDefault = "nats://localhost:4222"

	// SettingMongo is the config key for the mongo URL
	SettingMongo = "mongo_url"
	// SettingMongoDefault is the default value for the mongo URL
	SettingMongoDefault = "mongodb://mender-mongo:27017"

	// SettingDbName is the config key for the mongo database name
	SettingDbName = "mongo_dbname"
	// SettingDbNameDefault is the default value for the mongo database name
	SettingDbNameDefault = "deviceconnect"

	// SettingDbSSL is the config key for the mongo SSL setting
	SettingDbSSL = "mongo_ssl"
	// SettingDbSSLDefault is the default value for the mongo SSL setting
	SettingDbSSLDefault = false

	// SettingDbSSLSkipVerify is the config key for the mongo SSL skip verify setting
	SettingDbSSLSkipVerify = "mongo_ssl_skipverify"
	// SettingDbSSLSkipVerifyDefault is the default value for the mongo SSL skip verify setting
	SettingDbSSLSkipVerifyDefault = false

	// SettingDbUsername is the config key for the mongo username
	SettingDbUsername = "mongo_username"

	// SettingDbPassword is the config key for the mongo password
	SettingDbPassword = "mongo_password"

	// SettingDebugLog is the config key for the turning on the debug log
	SettingDebugLog = "debug_log"
	// SettingDebugLogDefault is the default value for the debug log enabling
	SettingDebugLogDefault = false

	// SettingDeviceAuthURL is the config key for the deviceauth url
	SettingDeviceAuthURL = "deviceauth_url"
	// SettingDeviceAuthURLDefault is the default value for the deviceauth url
	SettingDeviceAuthURLDefault = "http://mender-device-auth:8080"

	// SettingUseradmURL is the config key for the deviceauth url
	SettingUseradmURL = "useradm_url"
	// SettingUseradmURLDefault is the default value for the deviceauth url
	SettingUseradmURLDefault = "http://mender-useradm:8080"
)

var (
	// Defaults are the default configuration settings
	Defaults = []config.Default{
		{Key: SettingListen, Value: SettingListenDefault},
		{Key: SettingNatsURI, Value: SettingNatsURIDefault},
		{Key: SettingMongo, Value: SettingMongoDefault},
		{Key: SettingDbName, Value: SettingDbNameDefault},
		{Key: SettingDbSSL, Value: SettingDbSSLDefault},
		{Key: SettingDbSSLSkipVerify, Value: SettingDbSSLSkipVerifyDefault},
		{Key: SettingDebugLog, Value: SettingDebugLogDefault},
		{Key: SettingDeviceAuthURL, Value: SettingDeviceAuthURLDefault},
		{Key: SettingUseradmURL, Value: SettingUseradmURLDefault},
	}
)
