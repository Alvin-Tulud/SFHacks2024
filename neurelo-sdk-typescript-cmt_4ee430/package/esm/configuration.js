/* tslint:disable */
/* eslint-disable */
/**
 * Neurelo API Spec
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { BASE_PATH } from "./base";
var Configuration = /** @class */ (function () {
    function Configuration(param) {
        if (param === void 0) { param = {}; }
        this.apiKey = param.apiKey;
        this.username = param.username;
        this.password = param.password;
        this.accessToken = param.accessToken;
        this.basePath = param.basePath;
        this.serverIndex = param.serverIndex;
        this.baseOptions = param.baseOptions;
        this.formDataCtor = param.formDataCtor;
    }
    /**
     * Check if the given MIME is a JSON MIME.
     * JSON MIME examples:
     *   application/json
     *   application/json; charset=UTF8
     *   APPLICATION/JSON
     *   application/vnd.company+json
     * @param mime - MIME (Multipurpose Internet Mail Extensions)
     * @return True if the given MIME is JSON, false otherwise.
     */
    Configuration.prototype.isJsonMime = function (mime) {
        var jsonMime = new RegExp('^(application\/json|[^;/ \t]+\/[^;/ \t]+[+]json)[ \t]*(;.*)?$', 'i');
        return mime !== null && (jsonMime.test(mime) || mime.toLowerCase() === 'application/json-patch+json');
    };
    return Configuration;
}());
export { Configuration };
export var neureloConfig = new Configuration({
    apiKey: process.env.NEURELO_API_KEY || '',
    basePath: process.env.NEURELO_API_BASE_PATH || BASE_PATH,
    baseOptions: {
        headers: {
            'Content-Type': 'application/json',
        },
    },
});
